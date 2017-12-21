# -*- coding: utf-8 -*-
"""
    Sphinx Extension lilypond
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Allow Lilypond music notes to be included in Sphinx-generated documents
    inline and outline.

    :copyright: Copyright ©2009 by Wei-Wei Guo.
    :license: BSD, see LICENSE for details.

    The extension is modified from mathbase.py and pngmath.py by Sphinx team.

    Note: The extension has only very basic support for LaTeX builder.

    Further modified by @suitougreentea
    Change output format to SVG, Remove inline support,
    Add container and caption, and more.
    pdf2svg must be installed.
"""

import shutil
import tempfile
import posixpath
from os import path
from subprocess import Popen, PIPE
try:
    from hashlib import sha1 as sha
except ImportError:
    from sha import sha

from docutils import nodes, utils
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive

from sphinx.errors import SphinxError
from sphinx.util import ensuredir#from sphinx.directives import code

from sphinx.util import parselinenos
from sphinx.util.nodes import set_source_info

class LilyExtError(SphinxError):
    category = 'Lilypond extension error'

DOC_HEAD = r'''
\paper{
  indent = 0\mm
  line-width = 160\mm
  oddFooterMarkup = ##f
  oddHeaderMarkup = ##f
  bookTitleMarkup = ##f
  scoreTitleMarkup = ##f
}
'''

Directive_HEAD = r"""
"""

Directive_BACK = r"""
"""

class lily(nodes.Part, nodes.Element):
    pass

class LilyDirective(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        'nowrap': directives.flag,
        'linenos': directives.flag,
        'lineno-start': int,
        'emphasize-lines': directives.unchanged_required,
        'caption': directives.unchanged_required,
        'name': directives.unchanged,
        'without-code': directives.flag,
        'without-image': directives.flag,
    }

    def run(self):
        without_code = 'without-code' in self.options
        without_image = 'without-image' in self.options

        if not without_image:
            ## Generate LilyPond image node
            music = '\n'.join(self.content)
            lilyimage = lily()
            lilyimage['music'] = music
            lilyimage['docname'] = self.state.document.settings.env.docname
            lilyimage['nowrap'] = 'nowrap' in self.options

        if not without_code:
            ## Generate source code node (from sphinx.directives.code)
            # type: () -> List[nodes.Node]
            document = self.state.document
            code = u'\n'.join(self.content)
            location = self.state_machine.get_source_and_line(self.lineno)

            linespec = self.options.get('emphasize-lines')
            if linespec:
                try:
                    nlines = len(self.content)
                    hl_lines = parselinenos(linespec, nlines)
                    if any(i >= nlines for i in hl_lines):
                        logger.warning('line number spec is out of range(1-%d): %r' %
                                       (nlines, self.options['emphasize-lines']),
                                       location=location)

                    hl_lines = [x + 1 for x in hl_lines if x < nlines]
                except ValueError as err:
                    return [document.reporter.warning(str(err), line=self.lineno)]
            else:
                hl_lines = None

            literal = nodes.literal_block(code, code)
            literal['language'] = "lilypond"
            literal['linenos'] = 'linenos' in self.options or \
                                 'lineno-start' in self.options
            extra_args = literal['highlight_args'] = {}
            if hl_lines is not None:
                extra_args['hl_lines'] = hl_lines
            if 'lineno-start' in self.options:
                extra_args['linenostart'] = self.options['lineno-start']
            set_source_info(self, literal)

        ## Generate caption and container node
        caption = self.options.get('caption')
        if caption:
            caption_str = "LilyPond: %s" % caption
        else:
            caption_str = "LilyPond"
        caption_node = nodes.caption('', '', *[nodes.Text(caption_str)])

        container_node = nodes.container('', literal_block=True, classes=['lily-block-wrapper'])
        container_node += caption_node
        if not without_code: container_node += literal
        if not without_image: container_node += lilyimage

        self.add_name(container_node)

        return [container_node]

def render_lily(self, lily):
    """
    Render the Lilypond music expression *lily* using lilypond.
    """
    shasum = "%s.svg" % sha(lily.encode('utf-8')).hexdigest()
    relfn = posixpath.join(self.builder.imgpath, 'lily', shasum)
    outfn = path.join(self.builder.outdir, '_images', 'lily', shasum)
    if path.isfile(outfn):
        return relfn

    if hasattr(self.builder, '_lilypng'):
        return None, None

    music = '\\version "' + self.builder.config.pnglily_version + '"\n' + DOC_HEAD + self.builder.config.pnglily_preamble + lily
    if isinstance(music, str):
        music = music.encode('utf-8')

    # use only one tempdir per build -- the use of a directory is cleaner
    # than using temporary files, since we can clean up everything at once
    # just removing the whole directory (see cleanup_tempdir_lily)
    if not hasattr(self.builder, '_lilypng_tempdir'):
        tempdir = self.builder._lilypng_tempdir = tempfile.mkdtemp()
    else:
        tempdir = self.builder._lilypng_tempdir

    tf = open(path.join(tempdir, 'music.ly'), 'wb')
    tf.write(music)
    tf.close()

    ensuredir(path.dirname(outfn))
    # use some standard lilypond arguments
    lilypond_args = [self.builder.config.pnglily_lilypond]
    #lilypond_args += ['-o', tempdir, '--png']
    #lilypond_args += ['-o', tempdir, '-dpreview', '-dbackend=svg']
    lilypond_args += ['-dbackend=eps', '-dno-gs-load-fonts', '-dinclude-eps-fonts',
                      '-o', tempdir]
    # add custom ones from config value
    lilypond_args.extend(self.builder.config.pnglily_lilypond_args)

    # last, the input file name
    lilypond_args.append(path.join(tempdir, 'music.ly'))
    try:
        p = Popen(lilypond_args)#, stdout=PIPE, stderr=PIPE)
    except OSError as err:
        if err.errno != 2:   # No such file or directory
            raise
        self.builder.warn('lilypond command %r cannot be run (needed for music '
                          'display), check the pnglily_lilypond setting' %
                          self.builder.config.pnglily_lilypond)
        self.builder._lilypng_warned = True
        return None, None
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        raise LilyExtError(u'lilypond exited with error:\n[stderr]\n%s\n'
                           '[stdout]\n%s' % (stderr.decode('utf-8'), stdout.decode('utf-8')))
    a = Popen(["pdf2svg", path.join(tempdir, "music.pdf"), path.join(tempdir, "music.svg")])#, stdout=PIPE, stderr=PIPE)
    stdout, stderr = a.communicate()

    shutil.copyfile(path.join(tempdir, 'music.svg'), outfn)
    #Popen(['mogrify', '-trim', outfn], stdout=PIPE, stderr=PIPE)

    return relfn

def cleanup_tempdir_lily(app, exc):
    if exc:
        return
    if not hasattr(app.builder, '_lilypng_tempdir'):
        return
    try:
        shutil.rmtree(app.builder._lilypng_tempdir)
    except Exception:
        pass

def html_visit_lily(self, node):
    if node['nowrap']:
        music = node['music']
    else:
        music = Directive_HEAD #% (self.builder.config.pnglily_fontsize[1],
                               #   self.builder.config.pnglily_fontsize[1])
        music += node['music'] + Directive_BACK
    try:
        fname = render_lily(self, music)
    except LilyExtError as exc:
        sm = nodes.system_message(str(exc), type='WARNING', level=2,
                                  backrefs=[], source=node['music'])
        sm.walkabout(self)
        self.builder.warn('inline lilypond %r: ' % node['music'] + str(exc))
        raise nodes.SkipNode
    self.body.append(self.starttag(node, 'div', CLASS='lily'))
    # self.body.append('<p>')
    if fname is None:
        # something failed -- use text-only as a bad substitute
        self.body.append('<span class="lily">%s</span>' %
                         self.encode(node['music']).strip())
    else:
        self.body.append('<img src="%s" alt="%s" />\n</div>' %
                         (fname, self.encode(node['music']).strip()))
    # self.body.append('</p>')
    raise nodes.SkipNode

def setup(app):
    app.add_node(lily, html=(html_visit_lily, None))
    app.add_directive('lily', LilyDirective)
    app.add_config_value('pnglily_version', '2.19.59', False)
    app.add_config_value('pnglily_preamble', '', False)
    app.add_config_value('pnglily_fontsize', ['10', '0'], False)
    app.add_config_value('pnglily_lilypond', 'lilypond', False)
    app.add_config_value('pnglily_lilypond_args', [], False)
    app.connect('build-finished', cleanup_tempdir_lily)

import re
import sys
from docutils import nodes, utils, languages
from docutils.transforms import TransformError, Transform
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

from extensions.metanode import metanode

# Only number 3rd-nested section header.

class NodeVisitorCustomSectNum(nodes.GenericNodeVisitor):
    depth = 0
    enabled = True
    number = 1

    def default_visit(self, node):
        if isinstance(node, metanode) and node['type'] == 'custom_sect_num_start':
            self.enabled = True
            self.number = 1
        if isinstance(node, metanode) and node['type'] == 'custom_sect_num_end':
            self.enabled = False
        if isinstance(node, nodes.section):
            self.depth += 1
            if self.enabled and self.depth == 2:
                numbers = str(self.number)
                title = node[0]
                # Use &nbsp; for spacing:
                generated = nodes.inline('', '§' + str(numbers), classes=['sectnum'])
                title.insert(0, generated)
                title['auto'] = 1
                title['sectnum'] = self.number
                self.number += 1

    def default_departure(self, node):
        if isinstance(node, nodes.section):
            self.depth -= 1

class CustomSectNumTransform(Transform):

    """
    Automatically assigns numbers to the titles of document sections.
    It is possible to limit the maximum section level for which the numbers
    are added.  For those sections that are auto-numbered, the "autonum"
    attribute is set, informing the contents table generator that a different
    form of the TOC should be used.
    """

    default_priority = 710
    """Should be applied before `Contents`."""

    def apply(self):
        print(self.document.document)
        self.maxdepth = self.startnode.details.get('depth', None)
        self.startvalue = self.startnode.details.get('start', 1)
        self.prefix = self.startnode.details.get('prefix', '')
        self.suffix = self.startnode.details.get('suffix', '')
        self.startnode.parent.remove(self.startnode)
        if self.document.settings.sectnum_xform:
            if self.maxdepth is None:
                self.maxdepth = sys.maxsize
            self.update_section_numbers(self.document)
        else: # store details for eventual section numbering by the writer
            self.document.settings.sectnum_depth = self.maxdepth
            self.document.settings.sectnum_start = self.startvalue
            self.document.settings.sectnum_prefix = self.prefix
            self.document.settings.sectnum_suffix = self.suffix

    def update_section_numbers(self, node, depth=0, currentnumber=1):
        visitor = NodeVisitorCustomSectNum(node.document)
        node.walkabout(visitor)
        return

class CustomSectNumDirective(Directive):

    """Automatic section numbering."""

    option_spec = {'depth': int,
                   'start': int,
                   'prefix': directives.unchanged_required,
                   'suffix': directives.unchanged_required}

    def run(self):
        pending = nodes.pending(CustomSectNumTransform)
        pending.details.update(self.options)
        self.state_machine.document.note_pending(pending)

        return [pending]

class CustomSectNumStart(Directive):
    def run(self):
        node = metanode()
        node['type'] = 'custom_sect_num_start'
        return [node]

class CustomSectNumEnd(Directive):
    def run(self):
        node = metanode()
        node['type'] = 'custom_sect_num_end'
        return [node]

class NumberSection(Directive):
    def run(self):
        node = metanode()
        node['type'] = 'number_section'
        return [node]

def doctree_read(app, doctree):
    print("doctree-read event:")
    visitor = NodeVisitorCustomSectNum(doctree)
    doctree.walkabout(visitor)
    #for figure_info in doctree.traverse(figure):

def doctree_resolved(app, doctree, docname):
    print("doctree-resolved event:")
    #visitor = NodeVisitorCustomSectNum(doctree)
    #doctree.walkabout(visitor)

def setup(app):
    # app.add_transform(CustomSectNumTransform)
    app.add_directive('custom-sect-num', CustomSectNumDirective)
    app.add_directive('custom-sect-num-start', CustomSectNumStart)
    app.add_directive('custom-sect-num-end', CustomSectNumEnd)

    app.add_directive('num-section', NumberSection)

    #app.connect('doctree-read', doctree_read)
    #app.connect('doctree-resolved', doctree_resolved)

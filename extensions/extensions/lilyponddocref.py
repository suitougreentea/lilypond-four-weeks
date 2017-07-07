from docutils import nodes
import re

type_names = {
    "learning": "学習マニュアル",
    "notation": "記譜法リファレンス",
    "snippets": "スニペット",
    "internals": "内部リファレンス",
}

def lilypond_ref_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    ref_name = name[1:]
    type_name = type_names[ref_name]
    doc_version = inliner.document.settings.env.app.config.lily_doc_version
    re_match = re.search(r"(.+?) *<(.+)>", text)
    link_href = re_match.group(1)
    link_text = re_match.group(2)
    print(link_href)
    uri = "http://lilypond.org/doc/v%s/Documentation/%s/%s" % (doc_version, ref_name, link_href)
    rn = nodes.reference("", "%s: %s" % (type_name, link_text), internal=False, refuri=uri, classes=["ref_" + ref_name])
    return [rn], []

def lilypond_source_ref_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    committish = inliner.document.settings.env.app.config.lily_source_committish
    uri = "http://git.savannah.gnu.org/gitweb/?p=lilypond.git;a=blob;f=%s;hb=%s" % (text, committish)
    rn = nodes.reference("", "ソースコード: %s" % text, internal=False, refuri=uri, classes=["ref_source"])
    return [rn], []

def setup(app):
    app.add_config_value('lily_doc_version', None, 'env')
    app.add_config_value('lily_source_committish', None, 'env')
    app.add_role("rlearning", lilypond_ref_role)
    app.add_role("rnotation", lilypond_ref_role)
    app.add_role("rsnippets", lilypond_ref_role)
    app.add_role("rinternals", lilypond_ref_role)
    app.add_role("rsource", lilypond_source_ref_role)

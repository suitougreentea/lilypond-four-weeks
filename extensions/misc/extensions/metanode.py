from docutils.nodes import Part, Element, SkipNode

class metanode(Part, Element):
    """Dummy node indicates something. Should have `type` attribute."""
    pass

def visit_nothing(self, node):
    raise SkipNode

def setup(app):
    app.add_node(metanode, html=(visit_nothing, None))

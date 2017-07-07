def todo_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    inliner.reporter.warning("TODO here: " + text, line=lineno)
    return [], []

def setup(app):
    app.add_role("todo", todo_role)

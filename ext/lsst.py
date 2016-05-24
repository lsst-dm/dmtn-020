# Convenient linking to Docushare documents.

from docutils import nodes

def lsst_doc_role(name, rawtext, text, lineno, inliner, options=[], content={}):
    node = nodes.raw(rawtext,
                     "<a href=\"http://ls.st/%s-%s\">%s-%s</a>" %
                     (name, text, name.upper(), text),
                     format='html')
    return [node], []

def setup(app):
    app.add_role('ldm', lsst_doc_role)
    app.add_role('lse', lsst_doc_role)
    app.add_role('lpm', lsst_doc_role)


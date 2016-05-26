# Convenient linking to Docushare documents & JIRA tickets.

from docutils import nodes

def lsst_doc_role(name, rawtext, text, lineno, inliner,
                  options=None, content=None):
    node = nodes.reference(text="%s-%s" % (name.upper(), text),
                           refuri="http://ls.st/%s-%s" % (name, text))
    return [node], []

def lsst_jira_role(name, rawtext, text, lineno, inliner,
                   options=None, content=None):
    node = nodes.reference(text=text,
                           refuri="https://jira.lsstcorp.org/browse/"+text)
    return [node], []

def setup(app):
    app.add_role('ldm', lsst_doc_role)
    app.add_role('lse', lsst_doc_role)
    app.add_role('lpm', lsst_doc_role)
    app.add_role('jira', lsst_jira_role)

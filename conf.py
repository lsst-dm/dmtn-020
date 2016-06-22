#!/usr/bin/env python
#
# Sphinx configuration file
# see metadata.yaml in this repo for to update document-specific metadata

import os
import subprocess
from documenteer.designdocs import configure_sphinx_design_doc

# Ingest settings from metadata.yaml and use documenteer's
# configure_sphinx_design_doc to build a Sphinx configuration that is
# injected into this script's global namespace.
metadata_path = os.path.join(os.path.dirname(__file__), 'metadata.yaml')
with open(metadata_path, 'r') as f:
    confs = configure_sphinx_design_doc(f)
g = globals()
g.update(confs)

# Set last revision date based on git history
git_date = subprocess.check_output(["git", "log", "-1", "--date=short",
                                    "--pretty=%ad"]).decode().strip()
git_version = subprocess.check_output(["git", "log", "-1", "--date=short",
                                       "--pretty=%h"]).decode().strip()
if subprocess.check_output(["git", "status", "--porcelain"]).decode().strip():
    git_version += "-dirty"
g['html_context']['last_revised'] = "%s" % (git_date,)

extensions.append("documenteer.sphinxext")
intersphinx_mapping['dmdev'] = ('https://developer.lsst.io', None)

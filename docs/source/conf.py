import sys
import os.path

sys.path.append(os.path.abspath('../..'))

project = 'xxx'
copyright = '2023, asdf'
author = 'asdf'
release = 'asdf'

exclude_patterns = []

intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable/", None),
}


nitpicky = True
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
]

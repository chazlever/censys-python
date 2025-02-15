# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime

import sphinx_rtd_theme  # noqa

from censys.common import __version__

# -- Path setup --------------------------------------------------------------


sys.path.insert(0, os.path.abspath("../censys"))


# -- Project information -----------------------------------------------------

project = "Censys Python"
author = "Censys Team"
copyright = f"{datetime.now().year or 2021}, {author}"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.napoleon",
    "sphinx_rtd_theme",
    "sphinx-prompt",
    "sphinx_tabs.tabs",
    "sphinx_copybutton",
    "sphinxcontrib.autoprogram",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**tests**"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Theme Options
html_theme_options = {"style_external_links": False, "collapse_navigation": False}

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False


# -- Extension configuration -------------------------------------------------

# Sort members by type
# autodoc_member_order = "groupwise"

# Add mappings
intersphinx_mapping = {
    "requests": ("https://requests.readthedocs.io/en/latest/", None),
    "python": ("https://docs.python.org/3/", None),
}

# Prefix document path to section labels, otherwise autogenerated labels would look
# like 'heading' rather than 'path/to/file:heading'
autosectionlabel_prefix_document = True

# Define the prompt text that you’d like removed from copied text in your code blocks
copybutton_prompt_text = "$"

# Napoleon
napoleon_include_init_with_doc = False

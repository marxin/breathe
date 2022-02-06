# -*- coding: utf-8 -*-
#
# BreatheExample documentation build configuration file, created by
# sphinx-quickstart on Tue Feb  3 18:20:48 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import subprocess
import re

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
# sys.path.append(os.path.abspath('.'))

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ["breathe", "sphinx.ext.mathjax", "sphinx.ext.ifconfig"]

read_the_docs_build = os.environ.get("READTHEDOCS", None) == "True"
travis_build = os.environ.get("TRAVIS_CI", None) == "True"

# Get a description of the current position. Use Popen for 2.6 compat
git_tag = subprocess.Popen(["git", "describe", "--tags"], stdout=subprocess.PIPE).communicate()[0]

# convert from bytes to string
git_tag = git_tag.decode("ascii")

if travis_build:

    # Don't attempt to set the path as breathe is installed to virtualenv on travis

    # Set values with simple strings
    version = "'travis'"
    release = "'travis'"
    documentation_build = "travis"

elif read_the_docs_build:

    # On RTD we'll be in the 'source' directory
    sys.path.append("../../")

    # The version info for the project you're documenting, acts as replacement for
    # |version| and |release|, also used in various other places throughout the
    # built documents.
    #
    # The short X.Y version.
    version = "'unknown'"
    # The full version, including alpha/beta/rc tags.
    release = "'unknown'"

    # Check if it matches a pure tag number vX.Y.Z, rather than vX.Y.Z-91-g8676988 which is how
    # non-tagged commits are described (ie. relative to the last tag)
    if re.match(r"^v\d+\.\d+\.\d+$", git_tag):
        # git_tag is a pure version number (no subsequent commits)
        version = git_tag
        release = git_tag
        documentation_build = "readthedocs"

    else:
        version = "'latest'"
        release = "'latest'"
        documentation_build = "readthedocs_latest"

else:

    # For our usual dev build we'll be in the 'documentation' directory but Sphinx seems to set the
    # current working directory to 'source' so we append relative to that
    sys.path.append("../../")

    # Check if it matches a pure tag number vX.Y.Z, rather than vX.Y.Z-91-g8676988 which is how
    # non-tagged commits are described (ie. relative to the last tag)
    if re.match(r"^v\d+\.\d+\.\d+$", git_tag):
        # git_tag is a pure version number (no subsequent commits)
        version = git_tag
        release = git_tag
    else:
        version = "'latest'"
        release = "'latest'"

    documentation_build = "development"


# If we're doing a comparison then set the version & release to 'compare' so that they are always
# the same otherwise they can come up as changes when we really don't care if they are different.
comparison = os.environ.get("BREATHE_COMPARE", None) == "True"

if comparison:
    version = "compare"
    release = "compare"

# Only add spelling extension if it is available. We don't know if it is installed as we don't want
# to put it in the setup.py file as a dependency as we don't want Breathe to be dependent on it as
# people should be able to use Breathe without 'spelling'. There might be a better way to handle
# this.
try:
    import sphinxcontrib.spelling

    extensions.append("sphinxcontrib.spelling")
except ImportError:
    pass


# Configuration for spelling extension
spelling_word_list_filename = "spelling_wordlist.txt"
spelling_lang = "en_US"


# Configuration for mathjax extension
#
# Set path for mathjax js to a https URL as sometimes the Breathe docs are displayed under https
# and we can't load an http mathjax file from an https view of the docs. So we change to a https
# mathjax file which we can load from http or https. We break the url over two lines.
mathjax_path = (
    "https://c328740.ssl.cf1.rackcdn.com/" "mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
)


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Breathe"
copyright = "2009-2014, Michael Jones"


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
# unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Options for breathe extension
# -----------------------------

breathe_projects = {
    "class": "../../examples/doxygen/class/xml/",
    "classtest": "../../examples/specific/class/xml/",
    "struct": "../../examples/specific/struct/xml/",
    "interface": "../../examples/specific/interface/xml/",
    "decl_impl": "../../examples/specific/decl_impl/xml/",
    "structcmd": "../../examples/doxygen/structcmd/xml/",
    "tinyxml": "../../examples/tinyxml/tinyxml/xml/",
    "restypedef": "../../examples/doxygen/restypedef/xml/",
    "nutshell": "../../examples/specific/nutshell/xml/",
    "rst": "../../examples/specific/rst/xml/",
    "c_file": "../../examples/specific/c_file/xml/",
    "namespace": "../../examples/specific/namespacefile/xml/",
    "userdefined": "../../examples/specific/userdefined/xml/",
    "template_function": "../../examples/specific/template_function/xml/",
    "template_class": "../../examples/specific/template_class/xml/",
    "template_class_non_type": "../../examples/specific/template_class_non_type/xml/",
    "template_specialisation": "../../examples/specific/template_specialisation/xml/",
    "latexmath": "../../examples/specific/latexmath/xml/",
    "functionOverload": "../../examples/specific/functionOverload/xml/",
    "programlisting": "../../examples/specific/programlisting/xml/",
    "image": "../../examples/specific/image/xml/",
    "lists": "../../examples/specific/lists/xml/",
    "tables": "../../examples/specific/tables/xml/",
    "group": "../../examples/specific/group/xml/",
    "union": "../../examples/specific/union/xml/",
    "qtsignalsandslots": "../../examples/specific/qtsignalsandslots/xml/",
    "array": "../../examples/specific/array/xml/",
    "c_struct": "../../examples/specific/c_struct/xml/",
    "c_enum": "../../examples/specific/c_enum/xml/",
    "c_typedef": "../../examples/specific/c_typedef/xml/",
    "c_macro": "../../examples/specific/c_macro/xml/",
    "c_union": "../../examples/specific/c_union/xml/",
    "define": "../../examples/specific/define/xml/",
    "multifile": "../../examples/specific/multifilexml/xml/",
    "cpp_anon": "../../examples/specific/cpp_anon/xml/",
    "cpp_concept": "../../examples/specific/cpp_concept/xml/",
    "cpp_enum": "../../examples/specific/cpp_enum/xml/",
    "cpp_union": "../../examples/specific/cpp_union/xml/",
    "cpp_function": "../../examples/specific/cpp_function/xml/",
    "cpp_function_lookup": "../../examples/specific/cpp_function_lookup/xml/",
    "cpp_friendclass": "../../examples/specific/cpp_friendclass/xml/",
    "cpp_inherited_members": "../../examples/specific/cpp_inherited_members/xml/",
    "cpp_trailing_return_type": "../../examples/specific/cpp_trailing_return_type/xml/",
    "cpp_constexpr_hax": "../../examples/specific/cpp_constexpr_hax/xml/",
    "xrefsect": "../../examples/specific/xrefsect/xml/",
    "membergroups": "../../examples/specific/membergroups/xml/",
    "simplesect": "../../examples/specific/simplesect/xml/",
}

breathe_projects_source = {"auto": ("../../examples/specific", ["auto_function.h", "auto_class.h"])}

breathe_default_project = "tinyxml"

breathe_domain_by_extension = {
    "h": "cpp",
    "py": "py",
}

breathe_domain_by_file_pattern = {
    "class.h": "cpp",
    "alias.h": "c",
    "array.h": "c",
    "c_*.h": "c",
}

breathe_use_project_refids = True

# breathe_debug_trace_directives = True
# breathe_debug_trace_doxygen_ids = True
# breathe_debug_trace_qualification = True


# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
# html_style = 'default.css'

html_theme = "haiku"

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_use_modindex = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
# html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = "BreatheExampledoc"


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
    ("index", "BreatheExample.tex", "BreatheExample Documentation", "Michael Jones", "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True


def run_doxygen(folder):
    """Run the doxygen make command in the designated folder"""

    try:
        retcode = subprocess.call("cd %s; make DOXYGEN=doxygen" % folder, shell=True)
        if retcode < 0:
            sys.stderr.write("doxygen terminated by signal %s" % (-retcode))
    except OSError as e:
        sys.stderr.write("doxygen execution failed: %s" % e)


def generate_doxygen_xml(app):
    """Run the doxygen make commands if we're on the ReadTheDocs server"""

    read_the_docs_build = os.environ.get("READTHEDOCS", None) == "True"

    if read_the_docs_build:

        # Attempt to build the doxygen files on the RTD server. Explicitly override the path/name used
        # for executing doxygen to simply be 'doxygen' to stop the makefiles looking for the executable.
        # This is because the `which doxygen` effort seemed to fail when tested on the RTD server.
        run_doxygen("../../examples/doxygen")
        run_doxygen("../../examples/specific")
        run_doxygen("../../examples/tinyxml")


def setup(app):

    # Approach borrowed from the Sphinx docs
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )

    # Add hook for building doxygen xml when needed
    app.connect("builder-inited", generate_doxygen_xml)

    app.add_config_value("documentation_build", "development", True)

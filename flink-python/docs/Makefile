################################################################################
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

# Check if uv is available
ifeq ($(shell command -v uv >/dev/null 2>&1; echo $$?), 1)
$(error uv is not installed. Please install uv first: https://docs.astral.sh/uv/getting-started/installation/)
endif

# Set up virtual environment and Python paths
VENV_DIR = .venv
PYTHON = uv run python
SPHINXBUILD = uv run sphinx-build

# Check if virtual environment exists
ifeq ($(wildcard $(VENV_DIR)),)
$(info Virtual environment not found. Run 'make setup' to create it.)
endif

# The project depends on py4j, so py4j-*-src.zip should be set in PYTHONPATH.
py4j_lib = $(shell echo ../lib/py4j-*-src.zip)
export PYTHONPATH = $(realpath $(py4j_lib))

# You can set these variables from the command line.
SPHINXOPTS   ?=
PAPER        ?=
SOURCEDIR    ?= .
BUILDDIR     ?= _build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -j auto -d _build/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html dirhtml pickle json htmlhelp qthelp latex changes linkcheck doctest

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo ""
	@echo "Setup:"
	@echo "  setup     to create virtual environment and install dependencies"
	@echo "  setup-dev to create virtual environment and install dev dependencies"
	@echo ""
	@echo "Build:"
	@echo "  html      to make standalone HTML files"
	@echo "  dirhtml   to make HTML files named index.html in directories"
	@echo "  pickle    to make pickle files"
	@echo "  json      to make JSON files"
	@echo "  htmlhelp  to make HTML files and a HTML help project"
	@echo "  qthelp    to make HTML files and a qthelp project"
	@echo "  latex     to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  changes   to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck to check all external links for integrity"
	@echo "  doctest   to run all doctests embedded in the documentation (if enabled)"
	@echo ""
	@echo "Testing:"
	@echo "  test      to run all documentation tests"
	@echo "  test-doctest to run doctests in documentation"
	@echo "  doctest-fix to fix common doctest issues"
	@echo "  test-links to check all external links"
	@echo "  test-build to test documentation builds successfully"
	@echo "  test-notebooks to test Jupyter notebooks"
	@echo "  test-examples to test code examples"
	@echo ""
	@echo "Linting:"
	@echo "  lint      to run all linting tools (doc8, sphinx-lint, rstcheck)"
	@echo "  lint-fix  to run all linting tools with auto-fix (includes pre-commit)"
	@echo "  local-lint-fix to run all linting tools with auto-fix (local only, no pre-commit)"
	@echo "  auto-fix  to run automatic linting fixes"
	@echo "  doc8      to run doc8 RST linting"
	@echo "  sphinx-lint to run sphinx-lint"
	@echo "  rstcheck  to run rstcheck"
	@echo "  lint-code-blocks to lint Python code blocks in RST files"
	@echo "  lint-examples to lint Python files in examples/ directory"
	@echo "  lint-examples-fix to lint and fix Python files in examples/ directory"
	@echo "  pre-commit to run pre-commit hooks (includes auto-fix)"
	@echo ""
	@echo "Installation (legacy - use setup instead):"
	@echo "  install-dev  to install development dependencies"
	@echo "  install-lint to install linting dependencies"
	@echo "  install-spell to install spelling dependencies"

clean:
	-rm -rf _build/*

setup:
	@echo "Creating virtual environment and installing dependencies..."
	uv venv
	uv pip install -e .

setup-dev:
	@echo "Creating virtual environment and installing development dependencies..."
	uv venv
	uv pip install -e .[dev]

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) _build/html
	@echo
	@echo "Build finished. The HTML pages are in _build/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) _build/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in _build/dirhtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) _build/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) _build/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) _build/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in _build/htmlhelp."

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) _build/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in _build/qthelp, like this:"
	@echo "# qcollectiongenerator _build/qthelp/pyflinkdoc.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile _build/qthelp/pyflinkdoc.qhc"

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) _build/latex
	@echo
	@echo "Build finished; the LaTeX files are in _build/latex."
	@echo "Run \`make all-pdf' or \`make all-ps' in that directory to" \
	      "run these through (pdf)latex."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) _build/changes
	@echo
	@echo "The overview file is in _build/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) _build/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in _build/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) _build/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in _build/doctest/output.txt."

pdf: latex
	cd _build/latex && make all-pdf

pdf-html: pdf html
	cp _build/latex/pyflinkdoc.pdf _build/html

# Linting targets
lint: doc8 sphinx-lint rstcheck
	@echo "All linting checks completed."

lint-fix: auto-fix pre-commit
	@echo "All linting checks with auto-fix completed."

local-lint-fix: auto-fix doc8 sphinx-lint rstcheck lint-code-blocks lint-examples-fix
	@echo "All local linting checks with auto-fix completed (no pre-commit)."

auto-fix:
	@echo "Running automatic linting fixes..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	uv run python fix_lint.py

doc8:
	@echo "Running doc8 RST linting..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	uv run doc8 .

sphinx-lint:
	@echo "Running sphinx-lint..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	uv run sphinx-lint .

rstcheck:
	@echo "Running rstcheck..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	find . -name "*.rst" -not -path "./_build/*" -not -path "./.git/*" -exec uv run rstcheck {} +

pre-commit:
	@echo "Running pre-commit hooks with auto-fix..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	uv run pre-commit run --all-files

install-dev:
	@echo "Installing development dependencies..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' instead."; \
		exit 1; \
	fi
	uv pip install -e .[dev]

install-lint:
	@echo "Installing linting dependencies..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup' instead."; \
		exit 1; \
	fi
	uv pip install -e .[lint]

install-spell:
	@echo "Installing spelling dependencies..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup' instead."; \
		exit 1; \
	fi
	uv pip install -e .[spell]

# Testing targets
test: test-build test-doctest test-links test-notebooks test-examples
	@echo "All documentation tests completed."

test-doctest:
	@echo "Running doctests in documentation..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) _build/doctest
	@echo "Doctest results are in _build/doctest/output.txt"

doctest-fix:
	@echo "Fixing doctest issues in RST files..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	uv run ruff check --fix *.rst

lint-code-blocks:
	@echo "Linting Python code blocks in RST files..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	uv run python lint_code_blocks.py

test-links:
	@echo "Checking external links..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) _build/linkcheck
	@echo "Link check results are in _build/linkcheck/output.txt"

test-build:
	@echo "Testing documentation build..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) _build/test-html
	@echo "Build test completed successfully."

test-notebooks:
	@echo "Testing Jupyter notebooks..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	@if [ -d "interactive_examples" ]; then \
		find interactive_examples -name "*.ipynb" -exec uv run python -c "import nbformat; nbformat.read('{}', as_version=4)" \; ; \
		echo "Notebook validation completed."; \
	else \
		echo "No interactive_examples directory found."; \
	fi

test-examples:
	@echo "Testing code examples..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	uv run python -m pytest tests/ -v --tb=short

lint-examples:
	@echo "Linting Python files in the examples/ directory..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	uv run ruff check ../pyflink/examples/

lint-examples-fix:
	@echo "Linting and fixing Python files in the examples/ directory..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Virtual environment not found. Run 'make setup-dev' first."; \
		exit 1; \
	fi
	uv run ruff check --fix ../pyflink/examples/

"""
Tests for PyFlink documentation.

This module contains tests to validate the documentation quality,
structure, and content.
"""

import os
import re
import pytest
from pathlib import Path


class TestDocumentationStructure:
    """Test documentation structure and organization."""

    def test_required_files_exist(self):
        """Test that required documentation files exist."""
        required_files = [
            "index.rst",
            "conf.py",
            "README.md",
            "pyproject.toml",
            "Makefile",
        ]
        
        for file_name in required_files:
            assert Path(file_name).exists(), f"Required file {file_name} not found"

    def test_required_directories_exist(self):
        """Test that required documentation directories exist."""
        required_dirs = [
            "user_guide",
            "reference",
            "examples",
            "cookbook",
            "getting_started",
        ]
        
        for dir_name in required_dirs:
            assert Path(dir_name).is_dir(), f"Required directory {dir_name} not found"

    def test_index_files_exist(self):
        """Test that index.rst files exist in main directories."""
        index_dirs = [
            "user_guide",
            "reference",
            "examples",
            "cookbook",
            "getting_started",
        ]
        
        for dir_name in index_dirs:
            index_file = Path(dir_name) / "index.rst"
            assert index_file.exists(), f"index.rst not found in {dir_name}"


class TestRSTFiles:
    """Test RST file quality and structure."""

    def test_rst_files_have_license_header(self):
        """Test that RST files have proper license headers."""
        rst_files = list(Path(".").rglob("*.rst"))
        
        # Skip auto-generated files in reference/api/
        rst_files = [f for f in rst_files if "reference/api" not in str(f)]
        
        for rst_file in rst_files:
            with open(rst_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Check for Apache License header
                assert "Licensed to the Apache Software Foundation" in content, \
                    f"Missing license header in {rst_file}"

    def test_rst_files_no_trailing_whitespace(self):
        """Test that RST files don't have trailing whitespace."""
        rst_files = list(Path(".").rglob("*.rst"))
        
        # Skip auto-generated files in reference/api/
        rst_files = [f for f in rst_files if "reference/api" not in str(f)]
        
        for rst_file in rst_files:
            with open(rst_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    if line.rstrip() != line:
                        pytest.fail(f"Trailing whitespace in {rst_file}:{line_num}")

    def test_rst_files_end_with_newline(self):
        """Test that RST files end with a newline."""
        rst_files = list(Path(".").rglob("*.rst"))
        
        # Skip auto-generated files in reference/api/
        rst_files = [f for f in rst_files if "reference/api" not in str(f)]
        
        for rst_file in rst_files:
            with open(rst_file, 'r', encoding='utf-8') as f:
                content = f.read()
                assert content.endswith('\n'), f"File {rst_file} doesn't end with newline"


class TestCodeExamples:
    """Test code examples in documentation."""

    def test_python_code_blocks_syntax(self):
        """Test that Python code blocks have valid syntax."""
        rst_files = list(Path(".").rglob("*.rst"))
        
        # Skip auto-generated files in reference/api/
        rst_files = [f for f in rst_files if "reference/api" not in str(f)]
        
        for rst_file in rst_files:
            with open(rst_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Find Python code blocks
                code_blocks = re.findall(r'\.\. code-block:: python\n\n(.*?)(?=\n\n|\n[^ ]|\Z)', 
                                       content, re.DOTALL)
                
                for i, code_block in enumerate(code_blocks):
                    try:
                        # Try to compile the code
                        compile(code_block, f"{rst_file}:block_{i}", 'exec')
                    except SyntaxError as e:
                        pytest.fail(f"Syntax error in {rst_file} code block {i}: {e}")

    def test_literalinclude_files_exist(self):
        """Test that literalinclude files exist."""
        rst_files = list(Path(".").rglob("*.rst"))
        
        for rst_file in rst_files:
            with open(rst_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Find literalinclude directives
                includes = re.findall(r'\.\. literalinclude:: (.*?)\n', content)
                
                for include_path in includes:
                    # Resolve relative path from rst file
                    rst_dir = rst_file.parent
                    full_path = rst_dir / include_path
                    assert full_path.exists(), f"Literalinclude file not found: {full_path}"


class TestLinks:
    """Test internal and external links."""

    def test_internal_rst_links(self):
        """Test that internal RST links point to existing files."""
        rst_files = list(Path(".").rglob("*.rst"))
        
        for rst_file in rst_files:
            with open(rst_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Find internal links (doc:, ref:, etc.)
                internal_links = re.findall(r':doc:`([^`]+)`', content)
                internal_links.extend(re.findall(r':ref:`([^`]+)`', content))
                
                for link in internal_links:
                    # Skip external links and anchors
                    if link.startswith('http') or '#' in link:
                        continue
                    
                    # Check if the referenced file exists
                    link_path = Path(link)
                    if not link_path.suffix:
                        link_path = link_path.with_suffix('.rst')
                    
                    # Resolve relative to current file
                    full_path = rst_file.parent / link_path
                    assert full_path.exists(), f"Internal link not found in {rst_file}: {link}"


class TestConfiguration:
    """Test Sphinx configuration."""

    def test_conf_py_has_required_extensions(self):
        """Test that conf.py has required Sphinx extensions."""
        with open("conf.py", 'r', encoding='utf-8') as f:
            content = f.read()
            
        required_extensions = [
            'sphinx.ext.autodoc',
            'sphinx.ext.autosummary',
            'sphinx_mdinclude',
        ]
        
        for ext in required_extensions:
            assert ext in content, f"Required extension {ext} not found in conf.py"

    def test_pyproject_toml_has_required_dependencies(self):
        """Test that pyproject.toml has required dependencies."""
        with open("pyproject.toml", 'r', encoding='utf-8') as f:
            content = f.read()
            
        required_deps = [
            'sphinx>=4.0.0',
            'pydata_sphinx_theme>=0.8.0',
        ]
        
        for dep in required_deps:
            assert dep in content, f"Required dependency {dep} not found in pyproject.toml"


class TestInteractiveExamples:
    """Test interactive examples (Jupyter notebooks)."""

    def test_notebooks_exist(self):
        """Test that interactive examples directory exists and has notebooks."""
        interactive_dir = Path("interactive_examples")
        if interactive_dir.exists():
            notebooks = list(interactive_dir.rglob("*.ipynb"))
            assert len(notebooks) > 0, "No Jupyter notebooks found in interactive_examples"

    def test_notebooks_valid_format(self):
        """Test that notebooks have valid format."""
        interactive_dir = Path("interactive_examples")
        if interactive_dir.exists():
            notebooks = list(interactive_dir.rglob("*.ipynb"))
            
            for notebook in notebooks:
                try:
                    import nbformat
                    nbformat.read(notebook, as_version=4)
                except Exception as e:
                    pytest.fail(f"Invalid notebook format in {notebook}: {e}")


if __name__ == "__main__":
    pytest.main([__file__]) 
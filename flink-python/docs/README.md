# PyFlink Documentation

This directory contains the documentation for PyFlink, built using Sphinx.

## Quick Start

1. **Setup development environment:**
   ```bash
   make setup-dev
   ```

2. **Build documentation:**
   ```bash
   make html
   ```

3. **View the documentation:**
   Open `_build/html/index.html` in your browser.

## Linting and Code Quality

The documentation includes comprehensive linting tools to ensure high quality. There are several options depending on your needs:

### Basic Linting (Check Only)
```bash
make lint
```
Runs all linting tools in check-only mode:
- `doc8` - RST style checking
- `sphinx-lint` - Sphinx-specific linting
- `rstcheck` - RST syntax validation

### Auto-Fix with Pre-commit (Recommended for CI/CD)
```bash
make lint-fix
```
Runs comprehensive linting with auto-fix capabilities:
- Automatic fixes for common issues
- Pre-commit hooks for additional checks
- **Requires GitHub access** for pre-commit hooks

### Auto-Fix Local Only (No GitHub Required)
```bash
make local-lint-fix
```
Runs all linting with auto-fix using only local tools:
- Automatic fixes for common issues
- All local linting tools
- **No GitHub access required**
- Perfect for offline development or restricted environments

### Individual Linting Targets

You can also run specific linting tools:

```bash
# RST linting
make doc8
make sphinx-lint
make rstcheck

# Python code blocks in RST files
make lint-code-blocks

# Python examples directory
make lint-examples
make lint-examples-fix  # with auto-fix

# Automatic fixes only
make auto-fix
```

### When to Use Which Option

- **`make lint`** - Quick checks, no changes made
- **`make lint-fix`** - Full CI/CD pipeline, includes pre-commit hooks
- **`make local-lint-fix`** - Full auto-fix without external dependencies
- **Individual targets** - Specific tool checks or fixes

## Testing

Run comprehensive documentation tests:

```bash
make test
```

Individual test targets:
- `make test-doctest` - Test code examples in docs
- `make test-links` - Check external links
- `make test-build` - Verify builds work
- `make test-notebooks` - Test Jupyter notebooks
- `make test-examples` - Test code examples

## Development

### Adding New Documentation

1. Add RST files to appropriate directories
2. Update the index files to include new pages
3. Run `make lint` to check for issues
4. Run `make test` to ensure everything works

### Code Examples

- Place Python examples in `../pyflink/examples/`
- Use `literalinclude` in RST files to reference them
- Run `make lint-examples` to check example code quality

### Auto-Generated Documentation

The `reference/` directory contains auto-generated API documentation. These files are created by Sphinx's `autosummary` and `autodoc` extensions and should not be edited manually.

## Troubleshooting

### Pre-commit Issues
If you encounter GitHub-related errors with `make lint-fix`, use `make local-lint-fix` instead for local-only linting.

### Virtual Environment Issues
If you see "Virtual environment not found" errors, run:
```bash
make setup-dev
```

### Build Issues
If documentation fails to build, check:
1. All dependencies are installed: `make setup-dev`
2. No syntax errors in RST files: `make lint`
3. All referenced files exist: `make test-links` 
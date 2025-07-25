"""
Pytest configuration for documentation tests.
"""

import pytest
import sys
from pathlib import Path


@pytest.fixture(scope="session")
def docs_root():
    """Return the documentation root directory."""
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def rst_files(docs_root):
    """Return all RST files in the documentation."""
    rst_files = list(docs_root.rglob("*.rst"))
    # Skip auto-generated files in reference/api/
    return [f for f in rst_files if "reference/api" not in str(f)]


@pytest.fixture(scope="session")
def manual_rst_files(rst_files):
    """Return only manually written RST files (exclude auto-generated)."""
    return [f for f in rst_files if "reference/api" not in str(f)]


def pytest_configure(config):
    """Configure pytest for documentation testing."""
    # Add markers
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "structure: marks tests as structure validation tests"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test names."""
    for item in items:
        # Mark structure tests
        if "structure" in item.name.lower() or "Structure" in item.name:
            item.add_marker(pytest.mark.structure)
        
        # Mark integration tests
        if "integration" in item.name.lower() or "Integration" in item.name:
            item.add_marker(pytest.mark.integration)
        
        # Mark slow tests
        if any(slow_keyword in item.name.lower() for slow_keyword in 
               ["link", "build", "notebook", "example"]):
            item.add_marker(pytest.mark.slow) 
"""
Unit and regression test for the molssi_example package.
"""

# Import package, test suite, and other packages as needed
import molssi_example
import pytest
import sys

def test_molssi_example_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molssi_example" in sys.modules

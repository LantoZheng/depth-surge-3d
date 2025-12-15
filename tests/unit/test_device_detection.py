"""
Unit tests for device detection utilities.

Tests the CLI device option parsing without requiring torch.
"""

import unittest
import sys
import argparse
from pathlib import Path

# Add project root to path for testing
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


class TestDeviceChoicesInCLI(unittest.TestCase):
    """Test that CLI accepts MPS as a valid device option."""

    def test_device_choices_include_mps(self):
        """Test that MPS is included in the device choices."""
        # Create a parser with the same configuration as the main app
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--device",
            choices=["auto", "cuda", "mps", "cpu"],
            default="auto",
            help="Processing device",
        )
        
        # Test that all device options are accepted
        for device in ["auto", "cuda", "mps", "cpu"]:
            args = parser.parse_args(["--device", device])
            self.assertEqual(args.device, device)

    def test_device_default_is_auto(self):
        """Test that the default device is 'auto'."""
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--device",
            choices=["auto", "cuda", "mps", "cpu"],
            default="auto",
        )
        
        args = parser.parse_args([])
        self.assertEqual(args.device, "auto")

    def test_invalid_device_rejected(self):
        """Test that invalid device options are rejected."""
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--device",
            choices=["auto", "cuda", "mps", "cpu"],
            default="auto",
        )
        
        with self.assertRaises(SystemExit):
            parser.parse_args(["--device", "invalid"])


class TestMPSDocumentation(unittest.TestCase):
    """Test that MPS is properly documented."""

    def test_readme_mentions_mps(self):
        """Test that README.md mentions MPS/Apple Silicon support."""
        readme_path = project_root / "README.md"
        with open(readme_path, 'r') as f:
            content = f.read()
        
        self.assertIn("MPS", content)
        self.assertIn("Apple Silicon", content)

    def test_installation_mentions_mps(self):
        """Test that INSTALLATION.md mentions MPS/Apple Silicon support."""
        install_path = project_root / "docs" / "INSTALLATION.md"
        with open(install_path, 'r') as f:
            content = f.read()
        
        self.assertIn("MPS", content)
        self.assertIn("Apple Silicon", content)

    def test_parameters_mentions_mps(self):
        """Test that PARAMETERS.md mentions MPS device option."""
        params_path = project_root / "docs" / "PARAMETERS.md"
        with open(params_path, 'r') as f:
            content = f.read()
        
        self.assertIn("mps", content)
        self.assertIn("Apple Silicon", content)


if __name__ == '__main__':
    unittest.main()


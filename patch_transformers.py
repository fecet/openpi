#!/usr/bin/env python3
"""
Script to patch transformers library for openpi PyTorch support.

This script deletes target files before copying to avoid hardlink issues
that could affect the uv cache and other projects.
"""

import shutil
import site
import sys
from pathlib import Path


def main():
    # Define source and target directories
    source_dir = Path("src/openpi/models_pytorch/transformers_replace")

    # Find the site-packages directory (works with venv, pixi, conda, etc.)
    site_packages = None
    site_packages_paths = site.getsitepackages()

    # Look for the site-packages containing transformers
    for sp_path in site_packages_paths:
        sp = Path(sp_path)
        if (sp / "transformers").exists():
            site_packages = sp
            break

    if site_packages is None:
        print("Error: Could not find transformers installation in site-packages")
        print(f"Searched in: {site_packages_paths}")
        print("Make sure transformers is installed: pip install transformers")
        sys.exit(1)

    target_dir = site_packages / "transformers"

    # Verify directories exist
    if not source_dir.exists():
        print(f"Error: Source directory {source_dir} does not exist")
        sys.exit(1)

    if not target_dir.exists():
        print(f"Error: Target directory {target_dir} does not exist")
        print("Make sure transformers is installed: uv pip install transformers")
        sys.exit(1)

    print(f"Patching transformers library...")
    print(f"Source: {source_dir}")
    print(f"Target: {target_dir}")

    # Walk through source directory and copy files
    copied_files = []
    for source_file in source_dir.rglob("*"):
        if source_file.is_file():
            # Calculate relative path from source_dir
            relative_path = source_file.relative_to(source_dir)
            target_file = target_dir / relative_path

            # Create target directory if it doesn't exist
            target_file.parent.mkdir(parents=True, exist_ok=True)

            # Delete target file if it exists (to avoid hardlink issues)
            if target_file.exists():
                target_file.unlink()
                print(f"Deleted: {target_file}")

            # Copy the file
            shutil.copy2(source_file, target_file)
            copied_files.append(target_file)
            print(f"Copied: {relative_path}")

    print(f"\nSuccessfully patched {len(copied_files)} files in transformers library.")
    print(
        "\nWarning: This modifies the transformers library in your virtual environment."
    )
    print("To fully undo these changes, run: uv cache clean transformers")


if __name__ == "__main__":
    main()


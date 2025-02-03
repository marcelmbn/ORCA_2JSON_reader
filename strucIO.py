"""
This module contains routines for IO of structure files.
"""

from pathlib import Path


def xyzwriter(attype: str, filename: Path) -> None:
    """Write a single xyz file with the given attype and filename."""

    # Create the xyz file
    with open(filename, "w", encoding="utf8") as xyzfile:
        xyzfile.write("1\n")
        xyzfile.write("Generated by strucIO.py\n")
        xyzfile.write(attype + " 0.000000 0.000000 0.000000\n")
    xyzfile.close()

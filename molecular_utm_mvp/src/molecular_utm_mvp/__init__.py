"""
Molecular Universal Turing Machine MVP
=====================================

A prototype implementation using pylua_bioxen_vm_lib with social role personification.
"""

__version__ = "0.1.0"
__author__ = "Research Team"

from .core import MolecularUTM, UTMConfig
from .workers import WorkerRegistry
from .crn_engine import CRNEngine

__all__ = [
    "MolecularUTM",
    "UTMConfig", 
    "WorkerRegistry",
    "CRNEngine",
]

"""
Diplomatic Corps - Molecular FFI Integration Worker
==================================================

The Diplomatic Corps manages FFI integration with C/C++ libraries,
enabling high-performance molecular computations and external integrations.
"""

from .ffi_bridge import FFIBridge
from .c_integration import CIntegration
from .performance_optimizer import PerformanceOptimizer

__all__ = ["FFIBridge", "CIntegration", "PerformanceOptimizer"]

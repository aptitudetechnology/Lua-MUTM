#!/usr/bin/env python3
"""
Example benchmark execution
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from benchmarks.run_benchmarks import run_benchmark_suite


def main():
    """Run example benchmarks"""
    print("🧬 Running Example Molecular UTM Benchmarks")
    print("=" * 50)
    
    # Run small-scale benchmarks for demonstration
    results = run_benchmark_suite(
        problem_type="all",
        problem_size=5,  # Small size for quick demo
        debug=True
    )
    
    print("\n✅ Benchmark suite completed!")
    return results


if __name__ == "__main__":
    main()

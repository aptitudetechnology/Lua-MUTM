#!/usr/bin/env python3
"""
Molecular UTM Benchmark Runner
"""

import time
import asyncio
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from molecular_utm_mvp.core import MolecularUTM, UTMConfig
from benchmarks.tsp_benchmark import TSPBenchmark
from benchmarks.sat_benchmark import SATBenchmark


def run_benchmark_suite(problem_type="all", problem_size=10, debug=False):
    """Run the complete benchmark suite"""
    print("🧬 Starting Molecular UTM Benchmark Suite")
    print("=" * 50)
    
    config = UTMConfig(debug_mode=debug)
    utm = MolecularUTM(config)
    
    results = {}
    
    if problem_type in ["tsp", "all"]:
        print(f"\n📍 Running TSP Benchmark (size={problem_size})")
        tsp_benchmark = TSPBenchmark(utm)
        tsp_start = time.time()
        tsp_result = tsp_benchmark.run(problem_size)
        tsp_time = time.time() - tsp_start
        results["tsp"] = {"result": tsp_result, "time": tsp_time}
        print(f"TSP completed in {tsp_time:.2f}s")
    
    if problem_type in ["3sat", "all"]:
        print(f"\n🔧 Running 3-SAT Benchmark (size={problem_size})")
        sat_benchmark = SATBenchmark(utm)
        sat_start = time.time()
        sat_result = sat_benchmark.run(problem_size)
        sat_time = time.time() - sat_start
        results["3sat"] = {"result": sat_result, "time": sat_time}
        print(f"3-SAT completed in {sat_time:.2f}s")
    
    print("\n📊 Benchmark Results Summary:")
    print("=" * 30)
    for benchmark_name, data in results.items():
        print(f"{benchmark_name.upper()}: {data['time']:.2f}s - {data['result']}")
    
    return results


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Run Molecular UTM benchmarks')
    parser.add_argument('--problem', choices=['tsp', '3sat', 'all'], default='all')
    parser.add_argument('--size', type=int, default=10)
    parser.add_argument('--debug', action='store_true')
    
    args = parser.parse_args()
    run_benchmark_suite(args.problem, args.size, args.debug)

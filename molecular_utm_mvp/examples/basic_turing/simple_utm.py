#!/usr/bin/env python3
"""
Simple Universal Turing Machine Example
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from molecular_utm_mvp.core import MolecularUTM, UTMConfig


def main():
    """Run a simple UTM example"""
    print("🧬 Molecular UTM - Simple Example")
    print("=" * 40)
    
    # Initialize UTM with debug mode
    config = UTMConfig(debug_mode=True)
    utm = MolecularUTM(config)
    
    # Define a simple Turing machine that adds 1 to a binary number
    utm_program = """
    -- Simple binary increment UTM
    -- States: q0 (scan right), q1 (add one), qhalt
    -- Alphabet: 0, 1, blank (_)
    
    state_machine:add_transition("q0", "0", "q0", "0", "right")
    state_machine:add_transition("q0", "1", "q0", "1", "right")  
    state_machine:add_transition("q0", "_", "q1", "_", "left")
    
    state_machine:add_transition("q1", "0", "qhalt", "1", "stay")
    state_machine:add_transition("q1", "1", "q1", "0", "left")
    state_machine:add_transition("q1", "_", "qhalt", "1", "right")
    """
    
    # Set initial tape: "101_" (binary 5)
    initial_tape = {"0": "1", "1": "0", "2": "1", "3": "_"}
    
    print("Initial tape: 101 (binary 5)")
    print("Expected result: 110 (binary 6)")
    print()
    
    # Execute the UTM program
    result = utm.execute_utm_program(utm_program, initial_tape)
    
    print("Execution completed!")
    print(f"Final tape: {result['final_tape']}")
    print(f"Steps executed: {result['steps']}")
    print(f"Final state: {result['final_state']}")
    
    # Analyze molecular worker performance
    print("\n📊 Molecular Worker Statistics:")
    stats = utm.get_worker_statistics()
    for worker_name, worker_stats in stats.items():
        print(f"  {worker_name}: {worker_stats}")


if __name__ == "__main__":
    main()

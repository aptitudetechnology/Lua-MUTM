"""
3-SAT Problem Benchmark for Molecular UTM
"""

import random
from typing import List, Tuple


class SATBenchmark:
    """3-SAT benchmark using molecular UTM approach"""
    
    def __init__(self, molecular_utm):
        self.utm = molecular_utm
        self.variables = []
        self.clauses = []
    
    def generate_3sat_instance(self, num_vars: int, num_clauses: int = None):
        """Generate a random 3-SAT instance"""
        if num_clauses is None:
            num_clauses = int(4.3 * num_vars)  # Standard ratio for satisfiable instances
        
        self.variables = [f"x{i}" for i in range(num_vars)]
        self.clauses = []
        
        for _ in range(num_clauses):
            # Create clause with 3 random literals
            clause = []
            selected_vars = random.sample(range(num_vars), 3)
            
            for var_idx in selected_vars:
                # Randomly negate the variable
                negated = random.choice([True, False])
                clause.append((var_idx, negated))
            
            self.clauses.append(clause)
    
    def create_sat_crn(self) -> str:
        """Create CRN representation of 3-SAT problem"""
        crn_spec = """-- 3-SAT Chemical Reaction Network
-- Variables represented as molecular species (TRUE/FALSE states)
-- Clauses as reactions that must be satisfied

"""
        
        # Variable assignment reactions
        for var in self.variables:
            crn_spec += f"{var}_false -> {var}_true, rate=1.0\n"
            crn_spec += f"{var}_true -> {var}_false, rate=1.0\n"
        
        crn_spec += "\n-- Clause satisfaction reactions\n"
        
        # Clause satisfaction reactions
        for i, clause in enumerate(self.clauses):
            reactants = []
            for var_idx, negated in clause:
                var_name = self.variables[var_idx]
                state = "false" if negated else "true"
                reactants.append(f"{var_name}_{state}")
            
            # Clause is satisfied if at least one literal is true
            crn_spec += f"-- Clause {i+1}: {clause}\n"
            for reactant in reactants:
                crn_spec += f"{reactant} -> clause_{i}_satisfied, rate=10.0\n"
        
        return crn_spec
    
    def run(self, num_vars: int) -> dict:
        """Run 3-SAT benchmark with specified number of variables"""
        print(f"Generating 3-SAT instance with {num_vars} variables...")
        self.generate_3sat_instance(num_vars)
        
        print(f"Created {len(self.clauses)} clauses")
        print("Creating CRN specification...")
        crn_spec = self.create_sat_crn()
        
        print("Executing molecular 3-SAT solution...")
        result = self.utm.execute_crn_string(crn_spec)
        
        # Extract satisfying assignment
        assignment = self.extract_assignment(result)
        is_satisfiable = self.verify_assignment(assignment)
        
        return {
            "variables": num_vars,
            "clauses": len(self.clauses),
            "satisfiable": is_satisfiable,
            "assignment": assignment,
            "execution_steps": result.get("steps", 0)
        }
    
    def extract_assignment(self, utm_result) -> dict:
        """Extract variable assignment from UTM execution result"""
        # Simplified extraction - analyze molecular concentrations
        assignment = {}
        for var in self.variables:
            assignment[var] = random.choice([True, False])  # Placeholder
        return assignment
    
    def verify_assignment(self, assignment: dict) -> bool:
        """Verify if the assignment satisfies all clauses"""
        for clause in self.clauses:
            clause_satisfied = False
            for var_idx, negated in clause:
                var_name = self.variables[var_idx]
                var_value = assignment.get(var_name, False)
                
                # Check if this literal satisfies the clause
                if (not negated and var_value) or (negated and not var_value):
                    clause_satisfied = True
                    break
            
            if not clause_satisfied:
                return False
        
        return True

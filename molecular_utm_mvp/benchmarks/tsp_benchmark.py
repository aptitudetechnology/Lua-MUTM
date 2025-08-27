"""
Traveling Salesman Problem (TSP) Benchmark for Molecular UTM
"""

import random
import math
from typing import List, Tuple


class TSPBenchmark:
    """TSP benchmark using molecular UTM approach"""
    
    def __init__(self, molecular_utm):
        self.utm = molecular_utm
        self.cities = []
        self.distance_matrix = []
    
    def generate_cities(self, n: int) -> List[Tuple[float, float]]:
        """Generate n random cities"""
        self.cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]
        return self.cities
    
    def calculate_distance_matrix(self):
        """Calculate distance matrix between all cities"""
        n = len(self.cities)
        self.distance_matrix = [[0.0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    x1, y1 = self.cities[i]
                    x2, y2 = self.cities[j]
                    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
                    self.distance_matrix[i][j] = distance
    
    def create_tsp_crn(self, n: int) -> str:
        """Create CRN representation of TSP problem"""
        crn_spec = f"""
-- TSP Chemical Reaction Network for {n} cities
-- Each city is represented as a molecular species

-- City selection reactions
"""
        for i in range(n):
            for j in range(n):
                if i != j:
                    rate = 1.0 / (self.distance_matrix[i][j] + 1.0)  # Shorter distances = higher rates
                    crn_spec += f"city_{i} -> city_{j}, rate={rate:.3f}\n"
        
        return crn_spec
    
    def run(self, n: int) -> dict:
        """Run TSP benchmark with n cities"""
        print(f"Generating {n} cities...")
        self.generate_cities(n)
        self.calculate_distance_matrix()
        
        print("Creating CRN specification...")
        crn_spec = self.create_tsp_crn(n)
        
        print("Executing molecular TSP solution...")
        # Use molecular UTM to solve TSP
        result = self.utm.execute_crn_string(crn_spec)
        
        # Find best path from results
        best_path = self.extract_best_path(result)
        best_distance = self.calculate_path_distance(best_path)
        
        return {
            "cities": n,
            "best_path": best_path,
            "best_distance": best_distance,
            "execution_steps": result.get("steps", 0)
        }
    
    def extract_best_path(self, utm_result) -> List[int]:
        """Extract best path from UTM execution result"""
        # Simplified extraction - in real implementation would analyze molecular concentrations
        return list(range(len(self.cities)))  # Placeholder
    
    def calculate_path_distance(self, path: List[int]) -> float:
        """Calculate total distance of given path"""
        total_distance = 0.0
        for i in range(len(path)):
            current_city = path[i]
            next_city = path[(i + 1) % len(path)]
            total_distance += self.distance_matrix[current_city][next_city]
        return total_distance

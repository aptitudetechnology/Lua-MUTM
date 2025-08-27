# Visualizing Molecular UTM Concepts with Matplotlib

This guide illustrates key concepts from the Molecular Universal Turing Machine (UTM) MVP using Python's `matplotlib` library. These visualizations help explain the architecture, worker roles, and benchmark results for inclusion in your README.

## 1. Visualizing the Social Role Personification Model

```python
import matplotlib.pyplot as plt
import networkx as nx

# Define worker roles and relationships
roles = ["Librarian", "Inspector", "Foreman", "Shift Supervisor", "Diplomatic Corps"]
G = nx.DiGraph()
G.add_edges_from([
    ("Foreman", "Inspector"),
    ("Inspector", "Librarian"),
    ("Shift Supervisor", "Foreman"),
    ("Diplomatic Corps", "Foreman"),
    ("Diplomatic Corps", "Shift Supervisor"),
])

plt.figure(figsize=(8,6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, fontweight='bold', arrowsize=20)
plt.title("Molecular UTM Social Role Model")
plt.show()
```

## 2. Benchmark Results Visualization

Suppose you run TSP and 3-SAT benchmarks. You can visualize their execution times:

```python
import matplotlib.pyplot as plt

benchmarks = ['TSP', '3-SAT']
times = [2.3, 3.7]  # Example times in seconds

plt.bar(benchmarks, times, color=['#4e79a7', '#f28e2b'])
plt.ylabel('Execution Time (s)')
plt.title('Molecular UTM Benchmark Results')
plt.show()
```

## 3. Tape Operations (Librarian)

Visualize tape read/write operations:

```python
import matplotlib.pyplot as plt
import numpy as np

tape = np.zeros(20)
tape[5:10] = 1  # Simulate written data
plt.plot(tape, drawstyle='steps-mid')
plt.xlabel('Tape Position')
plt.ylabel('Symbol')
plt.title('Librarian Tape State')
plt.show()
```

## 4. State Transitions (Foreman)

```python
import matplotlib.pyplot as plt
import networkx as nx

states = ['START', 'READ', 'WRITE', 'HALT']
transitions = [('START', 'READ'), ('READ', 'WRITE'), ('WRITE', 'HALT')]
G = nx.DiGraph()
G.add_edges_from(transitions)
plt.figure(figsize=(6,4))
nx.draw(G, with_labels=True, node_color='lightgreen', node_size=1500, arrowsize=20)
plt.title('Foreman State Transitions')
plt.show()
```

---

**How to use:**
- Copy and run these code snippets in a Jupyter notebook or Python script after installing `matplotlib` and `networkx`.
- Use the generated plots in your documentation to visually explain the architecture and results.

**Install dependencies:**
```bash
pip install matplotlib networkx numpy
```

These visualizations will help readers understand the structure and performance of your Molecular UTM MVP.

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define color scheme for easy adjustment
colors = {
    'active': '#2E7D32',    # Green for active components
    'data': '#1976D2',      # Blue for data/metrics
    'warning': '#F57C00',   # Orange for warnings/high utilization
    'aux': '#6A1B9A',       # Purple for auxiliary elements
    'neutral': '#B0BEC5'    # Gray for backgrounds/inactive
}

# Create figure with 2x2 grid
fig = plt.figure(figsize=(12, 10))
plt.style.use('seaborn')  # Professional style

# Panel 1: Worker Role Relationships (Top Left)
ax1 = plt.subplot(2, 2, 1)
G = nx.DiGraph()
workers = ["Librarian", "Inspector", "Foreman", "Shift Supervisor", "Diplomatic Corps"]
G.add_edges_from([
    ("Foreman", "Inspector"),
    ("Inspector", "Librarian"),
    ("Shift Supervisor", "Foreman"),
    ("Diplomatic Corps", "Foreman"),
    ("Diplomatic Corps", "Shift Supervisor"),
])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=colors['active'], node_size=2000, 
        font_weight='bold', arrowsize=20, edge_color=colors['neutral'], ax=ax1)
ax1.set_title("Molecular UTM Worker Roles", fontsize=12, color=colors['data'])
for node, (x, y) in pos.items():
    ax1.text(x, y-0.1, f"80%", ha='center', va='top', color=colors['warning'], fontsize=10)

# Panel 2: Benchmark Performance (Top Right)
ax2 = plt.subplot(2, 2, 2)
benchmarks = ['TSP', '3-SAT']
times = [2.3, 3.7]  # Placeholder data
bars = ax2.bar(benchmarks, times, color=[colors['aux'], colors['data']])
ax2.set_ylabel('Execution Time (s)', color=colors['data'])
ax2.set_title('Benchmark Performance', fontsize=12, color=colors['data'])
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}s', ha='center', va='bottom', color=colors['neutral'])

# Panel 3: Tape State Visualization (Bottom Left)
ax3 = plt.subplot(2, 2, 3)
tape_positions = np.arange(20)
tape_data = np.zeros(20)
tape_data[5:10] = 1  # Placeholder data
ax3.plot(tape_positions, tape_data, drawstyle='steps-mid', color=colors['data'], lw=2)
ax3.set_xlabel('Tape Position', color=colors['data'])
ax3.set_ylabel('Symbol', color=colors['data'])
ax3.set_title('Librarian Tape State', fontsize=12, color=colors['data'])
ax3.axvline(x=10, color=colors['warning'], linestyle='--', label='Max Utilization')
ax3.legend()

# Panel 4: CRN Simulation (Bottom Right)
ax4 = plt.subplot(2, 2, 4)
time_points = np.arange(0, 60, 1)
species_a = np.sin(time_points / 10) + 1  # Placeholder data
species_b = np.cos(time_points / 10) + 1
ax4.plot(time_points, species_a, label='Species A', color=colors['data'])
ax4.plot(time_points, species_b, label='Species B', color=colors['aux'])
ax4.set_xlabel('Time (seconds)', color=colors['data'])
ax4.set_ylabel('Concentration', color=colors['data'])
ax4.set_title('CRN Species Concentrations', fontsize=12, color=colors['data'])
ax4.legend()

# Adjust layout and save
plt.tight_layout()
plt.savefig('molecular_utm_visualization.png', dpi=300, bbox_inches='tight')
plt.close()
import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define the variables
variables = [
    "Total Fantasy Points Scored", 
    "Positional Spending (QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST)", 
    "Player Ownership Percentage", 
    "Player Matchup Quality", 
    "Slate Context", 
    "Contest Size", 
    "Salary Efficiency"
]

# Add nodes to the graph
G.add_nodes_from(variables)

# Add edges to represent causal relationships
G.add_edges_from([
    ("Positional Spending (QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST)", "Total Fantasy Points Scored"),
    ("Player Ownership Percentage", "Total Fantasy Points Scored"),
    ("Player Ownership Percentage", "Positional Spending (QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST)"),
    ("Player Matchup Quality", "Total Fantasy Points Scored"),
    ("Player Matchup Quality", "Positional Spending (QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST)"),
    ("Slate Context", "Player Ownership Percentage"),
    ("Slate Context", "Player Matchup Quality"),
    ("Contest Size", "Player Ownership Percentage"),
    ("Salary Efficiency", "Total Fantasy Points Scored"),
    ("Salary Efficiency", "Positional Spending (QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST)")
])

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightgreen", font_size=10, font_weight="bold", edge_color="orange")
plt.title("Causal DAG for DraftKings Analysis", fontsize=16)
plt.show()
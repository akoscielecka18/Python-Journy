import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

#First drwaing
nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]

pos = {
    "E": (0, 0),
    "A": (0, 3),
    "B": (2.3, 1.9),
    "C": (2.9, -0.7),
    "D": (1.3, -2.7),
    "F": (-1.3, -2.7),
    "G": (-2.9, -0.7),
    "H": (-2.3, 1.9)
}
# matrix
matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0],  # A
    [0, 0, 0, 0, 1, 0, 0, 0],  # B
    [0, 0, 0, 0, 1, 0, 0, 0],  # C
    [0, 0, 0, 0, 1, 0, 0, 0],  # D
    [1, 1, 1, 1, 0, 1, 1, 1],  # E
    [0, 0, 0, 0, 1, 0, 0, 0],  # F
    [0, 0, 0, 0, 1, 0, 0, 0],  # G
    [0, 0, 0, 0, 1, 0, 0, 0]   # H
]

#create a table with row and column names
df = pd.DataFrame(matrix, index=nodes, columns=nodes)

# graf from matrix
G = nx.from_pandas_adjacency(df)

nx.draw(G, pos, node_color="black", node_size=500)
plt.show()
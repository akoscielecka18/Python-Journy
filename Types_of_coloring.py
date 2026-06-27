import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np

#graph with conflict- free connection
nodes = [r"$v_1$", r"$v_2$", r"$v_3$", r"$v_4$", r"$v_5$", r"$v_6$"]

pos = {
    r"$v_1$": (0, 3),
    r"$v_2$": (2.6, 1.0),
    r"$v_3$": (1.6, -2.3),
    r"$v_4$": (-1.6, -2.3),
    r"$v_5$": (-2.6, 1.0),
    r"$v_6$": (0, 0),
}

matrix = [
    [0, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0]
]

df = pd.DataFrame(matrix, index=nodes, columns=nodes)
G = nx.from_pandas_adjacency(df)

edge_color_map = {
    (r"$v_1$", r"$v_2$"): "red",
    (r"$v_1$", r"$v_5$"): "red",
    (r"$v_1$", r"$v_6$"): "red",
    (r"$v_2$", r"$v_3$"): "red",
    (r"$v_2$", r"$v_6$"): "purple",
    (r"$v_3$", r"$v_4$"): "red",
    (r"$v_3$", r"$v_6$"): "red",
    (r"$v_4$", r"$v_5$"): "purple",
    (r"$v_4$", r"$v_6$"): "purple",
    (r"$v_5$", r"$v_6$"): "purple",
}

edge_colors = []

for edge in G.edges():
    if edge in edge_color_map:
        edge_colors.append(edge_color_map[edge])
    elif (edge[1], edge[0]) in edge_color_map:
        edge_colors.append(edge_color_map[(edge[1], edge[0])])
    else:
        edge_colors.append("black")

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="black",
    font_color="white",
    node_size=500,
    font_size=14,
    edge_color=edge_colors,
    width=2
)
plt.axis("equal")
plt.show()

#proper coloring

edge_color_map1 = {
    (r"$v_1$", r"$v_2$"): "red",
    (r"$v_1$", r"$v_5$"): "red",
    (r"$v_1$", r"$v_6$"): "red",
    (r"$v_2$", r"$v_3$"): "purple",
    (r"$v_2$", r"$v_6$"): "purple",
    (r"$v_3$", r"$v_4$"): "red",
    (r"$v_3$", r"$v_6$"): "red",
    (r"$v_4$", r"$v_5$"): "purple",
    (r"$v_4$", r"$v_6$"): "purple",
    (r"$v_5$", r"$v_6$"): "red"
}

edge_colors = []

for edge in G.edges():
    if edge in edge_color_map1:
        edge_colors.append(edge_color_map1[edge])
    elif (edge[1], edge[0]) in edge_color_map1:
        edge_colors.append(edge_color_map1[(edge[1], edge[0])])
    else:
        edge_colors.append("black")

plt.figure()
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="black",
    font_color="white",
    node_size=500,
    font_size=14,
    edge_color=edge_colors,
    width=2
)

plt.axis("equal")
plt.show()
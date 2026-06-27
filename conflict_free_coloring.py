import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np

#graph with conflict- free connection
nodes = [r"$v_1$", r"$v_2$", r"$v_3$", r"$v_4$", r"$v_5$", r"$v_6$",
         r"$v_7$", r"$v_8$", r"$v_9$", r"$v_{10}$", r"$v_{11}$"]

pos = {
    r"$v_1$": (0, 0),
    r"$v_2$": (-2, -2),
    r"$v_3$": (2, -2),
    r"$v_4$": (-3, -3),
    r"$v_5$": (-4, -4),
    r"$v_6$": (-6, -6),
    r"$v_7$": (-2, -6),
    r"$v_8$": (2, -3),
    r"$v_9$": (2, -5),
    r"$v_{10}$": (4, -5),
    r"$v_{11}$": (4, -3)
}

matrix = [
    [0, 1, 1, 0, 0, 0,0, 0,0,0,0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0,1, 0,0,0,0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
]

df = pd.DataFrame(matrix, index=nodes, columns=nodes)
G = nx.from_pandas_adjacency(df)
plt.figure()
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="black",
    font_color="white",
    node_size=500,
    font_size=14,
    width=2
)
plt.axis("equal")
plt.show()

#subgraph
nodes1 = [r"$v_2$", r"$v_3$", r"$v_4$", r"$v_5$", r"$v_8$"]

pos1 = {
    r"$v_2$": (-2, -2),
    r"$v_3$": (2, -2),
    r"$v_4$": (-3, -3),
    r"$v_5$": (-4, -4),
    r"$v_8$": (2, -3)
}

matrix1 = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    ]

df1 = pd.DataFrame(matrix1, index=nodes1, columns=nodes1)
G1 = nx.from_pandas_adjacency(df1)
plt.figure()
nx.draw(
    G1,
    pos1,
    with_labels=True,
    node_color="black",
    font_color="white",
    node_size=500,
    font_size=14,
    width=2
)
plt.axis("equal")
plt.show()

#graph with conflict- free connection other example
nodes2 = [r"$v_1$", r"$v_2$", r"$v_3$", r"$v_4$", r"$v_5$", r"$v_6$",
         r"$v_7$", r"$v_8$", r"$v_9$", r"$v_{10}$", r"$v_{11}$", r"$v_{12}$", r"$v_{13}$"]

pos2 = {
    r"$v_1$": (0, 0),
    r"$v_2$": (-2, -2),
    r"$v_3$": (2, -2),
    r"$v_4$": (-3, -3),
    r"$v_5$": (-4, -4),
    r"$v_6$": (-6, -6),
    r"$v_7$": (-2, -6),
    r"$v_8$": (2, -3),
    r"$v_9$": (2, -4),
    r"$v_{10}$": (2, -6),
    r"$v_{11}$": (2, -8),
    r"$v_{12}$": (4, -8),
    r"$v_{13}$": (4, -6)
}

matrix2 = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,0,0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,0,0],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,0,0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,0,0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0,0,0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0,0,0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,0,0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1,0,0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0,1,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0,1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,1,0]
]

df2 = pd.DataFrame(matrix2, index=nodes2, columns=nodes2)
G2 = nx.from_pandas_adjacency(df2)
plt.figure()
nx.draw(
    G2,
    pos2,
    with_labels=True,
    node_color="black",
    font_color="white",
    node_size=500,
    font_size=14,
    width=2
)
plt.axis("equal")
plt.show()

#------------------------
nodes3 = [r"$v_1$", r"$v_2$", r"$v_3$", r"$v_4$", r"$v_5$", r"$v_6$",
          r"$v_7$", r"$v_8$", r"$v_9$", r"$v_{10}$", r"$v_{11}$", r"$v_{12}$", r"$v_{13}$"]

pos3 = {
    r"$v_1$": (0, 0),
    r"$v_2$": (-2, -2),
    r"$v_3$": (2, -2),
    r"$v_4$": (-3, -3),
    r"$v_5$": (-4, -4),
    r"$v_6$": (-6, -6),
    r"$v_7$": (-2, -6),
    r"$v_8$": (2, -3),
    r"$v_9$": (2, -4),
    r"$v_{10}$": (2, -6),
    r"$v_{11}$": (2, -8),
    r"$v_{12}$": (4, -8),
    r"$v_{13}$": (4, -6)
}

# Krawędzie grafu
edges3 = [
    (r"$v_1$", r"$v_2$"),
    (r"$v_1$", r"$v_3$"),
    (r"$v_2$", r"$v_3$"),
    (r"$v_2$", r"$v_4$"),
    (r"$v_4$", r"$v_5$"),
    (r"$v_5$", r"$v_6$"),
    (r"$v_6$", r"$v_7$"),
    (r"$v_7$", r"$v_5$"),
    (r"$v_3$", r"$v_8$"),
    (r"$v_8$", r"$v_9$"),
    (r"$v_9$", r"$v_{10}$"),
    (r"$v_{10}$", r"$v_{11}$"),
    (r"$v_{11}$", r"$v_{12}$"),
    (r"$v_{12}$", r"$v_{13}$"),
    (r"$v_{13}$", r"$v_{10}$")
]

G3 = nx.Graph()
G3.add_nodes_from(nodes3)
G3.add_edges_from(edges3)

# Pomocniczo: klucz dla krawędzi nieskierowanych
def e(u, v):
    return frozenset((u, v))

# Kolorowanie krawędzi
edge_colors_map = {
    # zielone
    e(r"$v_1$", r"$v_2$"): "green",
    e(r"$v_6$", r"$v_7$"): "green",
    e(r"$v_{11}$", r"$v_{12}$"): "green",

    # fioletowe
    e(r"$v_4$", r"$v_5$"): "purple",
    e(r"$v_3$", r"$v_8$"): "purple",
    e(r"$v_9$", r"$v_{10}$"): "purple",

    # czerwone
    e(r"$v_1$", r"$v_3$"): "red",
    e(r"$v_2$", r"$v_3$"): "red",
    e(r"$v_2$", r"$v_4$"): "red",
    e(r"$v_5$", r"$v_6$"): "red",
    e(r"$v_5$", r"$v_7$"): "red",
    e(r"$v_8$", r"$v_9$"): "red",
    e(r"$v_{10}$", r"$v_{11}$"): "red",
    e(r"$v_{12}$", r"$v_{13}$"): "red",
    e(r"$v_{13}$", r"$v_{10}$"): "red"
}

edge_colors = [edge_colors_map[e(u, v)] for (u, v) in G3.edges()]

plt.figure(figsize=(10, 7))

nx.draw_networkx_nodes(
    G3, pos3,
    node_color="black",
    node_size=700
)

nx.draw_networkx_labels(
    G3, pos3,
    font_color="white",
    font_size=14
)

nx.draw_networkx_edges(
    G3, pos3,
    edge_color=edge_colors,
    width=3
)

plt.axis("equal")
plt.axis("off")
plt.show()
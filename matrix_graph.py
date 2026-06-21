import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

#First drwaing
#maths symbols to show indexes
nodes = [r"$v_1$", r"$v_2$", r"$v_3$", r"$v_4$", r"$v_5$", r"$v_6$", r"$v_7$", r"$v_8$"]

pos = {
    r"$v_5$": (0, 0),
    r"$v_1$": (0, 3),
    r"$v_2$": (2.3, 1.9),
    r"$v_3$": (2.9, -0.7),
    r"$v_4$": (1.3, -2.7),
    r"$v_6$": (-1.3, -2.7),
    r"$v_7$": (-2.9, -0.7),
    r"$v_8$": (-2.3, 1.9)
}
# matrix
matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0]
]

#create a table with row and column names
df = pd.DataFrame(matrix, index=nodes, columns=nodes)

# graf from matrix
G = nx.from_pandas_adjacency(df)

fig, ax = plt.subplots(figsize=(8, 6))
ax.axis("off")

table = ax.table(
    cellText=matrix,
    rowLabels=nodes,
    colLabels=nodes,
    loc="center",
    cellLoc="center",
    edges="open",
    bbox=[0.18, 0.12, 0.70, 0.70]
)

table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.5)

plt.title("Macierz sąsiedztwa", pad=20)
plt.savefig("macierz_sasiedztwa.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure()
nx.draw(G, pos, node_color="black", node_size=500)
plt.show()

#---------------------------------
#how incidence matrix looks like
vertices = [r"$v_1$", r"$v_2$", r"$v_3$", r"$v_4$",
            r"$v_5$", r"$v_6$", r"$v_7$", r"$v_8$"]

edges = [r"$e_1$", r"$e_2$", r"$e_3$", r"$e_4$",
         r"$e_5$", r"$e_6$", r"$e_7$"]

incidence_matrix = [
    [1, 0, 0, 0, 0, 0, 0],  # v1
    [0, 1, 0, 0, 0, 0, 0],  # v2
    [0, 0, 1, 0, 0, 0, 0],  # v3
    [0, 0, 0, 1, 0, 0, 0],  # v4
    [1, 1, 1, 1, 1, 1, 1],  # v5
    [0, 0, 0, 0, 1, 0, 0],  # v6
    [0, 0, 0, 0, 0, 1, 0],  # v7
    [0, 0, 0, 0, 0, 0, 1]   # v8
]
df1 = pd.DataFrame(incidence_matrix, index=vertices, columns=edges)

fig1, ax1 = plt.subplots(figsize=(7, 5))
ax1.axis("off")

table1 = ax1.table(
    cellText=incidence_matrix,
    rowLabels=vertices,
    colLabels=edges,
    loc="center",
    cellLoc="center",
    edges="open",
    bbox=[0.18, 0.12, 0.70, 0.70]
)

table1.auto_set_font_size(False)
table1.set_fontsize(12)
table1.scale(1.2, 1.5)

ax1.set_title("Macierz incydencji", pad=20)

plt.savefig("macierz_incydencji.png", dpi=300, bbox_inches="tight")
plt.show()

G1 = nx.Graph()
G1.add_nodes_from(vertices)

# dla każdej kolumny, czyli dla każdej krawędzi e_i
for edge in df1.columns:
    # szukamy wierzchołków, które mają 1 w tej kolumnie
    connected_vertices = df1.index[df1[edge] == 1].tolist()

    # każda zwykła krawędź łączy dokładnie dwa wierzchołki
    if len(connected_vertices) == 2:
        u = connected_vertices[0]
        v = connected_vertices[1]

        # dodajemy krawędź i zapisujemy jej nazwę jako label
        G1.add_edge(u, v, label=edge)

pos1 = {
    r"$v_5$": (0, 0),
    r"$v_1$": (0, 3),
    r"$v_2$": (2.3, 1.9),
    r"$v_3$": (2.9, -0.7),
    r"$v_4$": (1.3, -2.7),
    r"$v_6$": (-1.3, -2.7),
    r"$v_7$": (-2.9, -0.7),
    r"$v_8$": (-2.3, 1.9)
}

plt.figure(figsize=(7, 6))

# rysujemy wierzchołki i krawędzie
nx.draw(
    G1,
    pos1,
    with_labels=True,
    node_color="lightblue",
    node_size=1000,
    font_size=12
)

# podpisy krawędzi, czyli e_1, e_2, ...
edge_labels = nx.get_edge_attributes(G1, "label")

nx.draw_networkx_edge_labels(
    G1,
    pos1,
    edge_labels=edge_labels,
    font_size=12,
    rotate=False
)

plt.title("Graf z macierzy incydencji")
plt.show()
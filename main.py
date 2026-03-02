import matplotlib.pyplot as plt
import networkx as nx

G=nx.Graph()
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

nx.draw(G)
plt.show()
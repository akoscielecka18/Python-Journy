import matplotlib.pyplot as plt
import networkx as nx

# Part 1:
G=nx.Graph()
#adding nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

#everytime nodes will be in the same spot
pos = nx.spring_layout(G, seed=42)

#drawing graph
plt.figure()
nx.draw(G, pos)
plt.show()

#-----------------------------
#changing color of the nodes
plt.figure()
nx.draw(G,pos, node_color="black")
plt.show()

#-----------------------------
#changing size of the nodes
plt.figure()
nx.draw(G,pos, node_size=100)
plt.show()

#-----------------------------
#adding edges
G.add_edge( "A", "B" )
G.add_edge("B", "C")

plt.figure()
nx.draw(G,pos)
plt.show()

#-----------------------------
#changing size/color of edges
plt.figure()
nx.draw(G,pos, edge_color="blue", width = 0.2)
plt.show()

#-----------------------------
#adding rest of the edges
G.add_edge( "C", "D" )
G.add_edge("D", "E")
G.add_edge("E", "A")

plt.figure()
nx.draw(G,pos, edge_color="blue", width = 0.2)
plt.show()

#-----------------------------
#adding labels to nodes
plt.figure()
nx.draw(G,pos, with_labels=True)
plt.show()

# Part 1:

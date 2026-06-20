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

# Part 2:
#adding nodes
G1=nx.Graph()
G1.add_nodes_from(["A","B","C","D","E", "F"])

#other way of adding edges
G1.add_edges_from([("A","B"),("B","C"),("C", "D"), ("D", "E"), ("E", "F"), ("F", "A")])

plt.figure()
nx.draw(G1, with_labels=True)
plt.show()

#-----------------------------
#other way to adding nodes
G2=nx.Graph()
G2.add_nodes_from("ABCDEFG")

#other way of adding edges
G2.add_edges_from(["AB","BC","CD","DE","EF","FG","GA"])
plt.figure()
nx.draw(G2, with_labels=True)
plt.show()

#-----------------------------
#other way to adding nodes
G3=nx.Graph()
G3.add_nodes_from([1,2,3,4,5,6])

#other way of adding edges
G3.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,6),(6,1)])
plt.figure()
nx.draw(G3, with_labels=True)
plt.show()

# Part 3:
#adding attributes to nodes and edges
G = nx.Graph()
G.add_node("A", Age =12, Gender = "F")
G.add_node("B", Age =18, Gender = "M")
G.add_node("C", Age =19, Gender = "F")
G.add_node("D", Age =20, Gender = "M")
G.add_node("E", Age =21, Gender = "F")

G.add_edge("A", "B", weight = 3)
G.add_edge("B", "C", weight = 0.5)
G.add_edge("C", "D", weight = 6)
G.add_edge("D", "E", weight = 12)
G.add_edge("E", "A", weight = "PINK")

#see what kind of features has node A
print(G.nodes["A"])
#see what kind of features has edge AB
print(G.edges["A","B"])

#naming graf
G.graph["Name"] = "My Graph"
print(G.graph)

#other method to define attributes
G1 = nx.Graph()
G1.add_nodes_from([
    ("A", {"Age": 12, "Gender": "F"}),
    ("B", {"Age": 18, "Gender": "M"}),
    ("C", {"Age": 19, "Gender": "F"}),
    ("D", {"Age": 20, "Gender": "M"}),
    ("E", {"Age": 21, "Gender": "F"})
])

G1.add_edges_from([
    ("A", "B", {"weight": 3}),
    ("B", "C", {"weight": 6}),
    ("C", "D", {"weight": 12}),
    ("D", "E", {"weight": 6}),
    ("E", "F", {"weight": 12}),
    ("F", "A", {"weight": 6})
])

print(G1.edges[("C","D")])
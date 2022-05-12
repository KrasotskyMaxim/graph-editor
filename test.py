import networkx as nx
import matplotlib.pyplot as plt


# G1 = nx.Graph(graph_name="G1-name")
# G1.add_node("A", data="A data")
# G1.add_nodes_from(["B", "C"])
# G1.add_nodes_from([
#     (1, {'color': "red"}),
#     (2, {'color': "green"})
# ])

# G2 = nx.path_graph(10)
# G1.add_nodes_from(G2)

# G1.add_edge("A", "C")
# e = (1, 1)
# G1.add_edge(*e)
# G1.add_edges_from([("B", "A", {'weight': 3.1415})])

# print("Nodes: ", list(G1.nodes))
# print("Edges: ", list(G1.edges(["A", 1])))
# print("Adj 'A': ", G1.adj["A"])
# print("Degree 1: ", G1.degree())

# G1.remove_node("B")
# G1.remove_nodes_from([5, 6, 7])
# print("Nodes: ", list(G1.nodes))

# G1.add_edge(2, 3)
# G1[2][3]['color'] = "yellow"
# print(G1[2][3])

# print(G1.graph['graph_name'])
# print(G1.nodes.data())

# G1.nodes["A"]['data'] = 'hello'
# print('data: ', G1.nodes["A"]['data'])

# GG = nx.DiGraph()

# GG.add_node(1)
# GG.add_node(2)
# GG.add_node(3)

# GG.add_edge(1, 1)
# GG.add_edge(2, 3)
# GG.add_edge(3, 2)

# res = list(nx.eulerian_path(GG))
# print(res)
# if res[0][0] == res[-1][1]:
#     print("Eyler cycle!")

G = nx.complete_graph(4)
for path in nx.all_simple_paths(G, source=1, target=2):
    print(path)
    
print(nx.shortest_path(G, source=1, target=2), nx.shortest_path_length(G, source=1, target=2))
    
nx.draw(G, with_labels=True)
plt.show()
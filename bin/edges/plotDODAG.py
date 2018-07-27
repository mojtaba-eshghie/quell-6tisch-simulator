import networkx as nx
import json
from matplotlib import pyplot as plt
graph = nx.Graph()

#the per results file is for quell!!!
with open('topo.json', 'r') as topo:
    with open('edges.json', 'r') as edges:
        data = json.load(topo)
        edges_dictionary = json.load(edges)
        print(edges_dictionary)
        for node in data:
            pos_x, pos_y = data[node]
            pos_x = round(pos_x, 4)
            pos_y = round(pos_y, 4)
            graph.add_node(int(node), pos=(pos_x, pos_y))

        for element in edges_dictionary:
            graph.add_edge(int(element), edges_dictionary[element])

        positions = nx.get_node_attributes(graph, 'pos')
        nx.draw_networkx(graph, positions, node_size=200)
        plt.title('quell')
        plt.show()

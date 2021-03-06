import networkx as nx
import matplotlib.pyplot as plt

from graph_editor.console.model.graph_errors import *


class ConsoleGraph:
    _path_to_save = './graph_editor/saved_graphs/'
    _type_edges = ['--', '<-', '->']
    _DEFAULT_COLOR = 'blue'
    
    def __init__(self, *args, **kwargs):
        self.is_full = False
        self.color_map = []
        self.graph = nx.DiGraph()
        if kwargs.get('name'):
            self.graph.graph['name'] = kwargs['name']
        if kwargs.get('nodes'):
            self.graph.add_nodes_from(kwargs['nodes'].split())
        if kwargs.get('edges'):
            self.parse_edges(edges=kwargs['edges'])        

    def parse_edges(self, edges):
        edges = edges.split()
        
        for e in edges:
            for type_e in self._type_edges:
                if type_e in e:
                    if type_e == '--':
                        e1 = tuple(e.split(type_e))
                        e2 = tuple(reversed(e1))
                        edge = [e1, e2]
                    else:   
                        edge = [tuple(e.split(type_e))]
                    break
            if edge:
                self.graph.add_edges_from(edge)
            else:
                raise EdgeError
            
    @property
    def name(self):
        return self.graph.graph['name']
    
    @property
    def nodes(self):
        return self.graph.nodes
    
    @property 
    def edges(self):
        return self.graph.edges
        
    @property
    def info(self):
        return f'''
        Graph: {self.name}\n
        nodes: {self.nodes}\n
        edges: {self.edges}\n
        nodes degree:\n{self.show_nodes_degree()}
        is complete: {self.is_full}
        '''
    
    def show_nodes_degree(self):
        degrees = self.graph.degree()
        nodes_degree_string = ""
        for node, degree in degrees:
            nodes_degree_string += f'node is {node} and degree is {degree}\n'
        return nodes_degree_string
    
    def save_to_gml(self, path):
        nx.write_gml(self.graph, self._path_to_save+path+'.gml')
        return True 
        
    def load_from_gml(self, path):
        self.graph = nx.read_gml(self._path_to_save+path+'.gml')
        return self.name
    
    def set_node_data(self, node, data):
        if data:
            data_key, data_value = tuple(data.split('--'))
            self.graph.nodes[node][data_key] = data_value
        return True
    
    def add_node(self, node_name, node_data):
        self.graph.add_node(node_name)
        self.set_node_data(node=node_name, data=node_data)
        return True
    
    def show_in_label(self):
        self.update_color_map()
        plt.figure(self.name)
        nx.draw(self.graph, node_color=self.color_map, with_labels=True, font_weight='bold')
        plt.show()
        
    def delete_node(self, node_name):
        if node_name not in self.nodes:
            return 
        
        self.graph.remove_node(node_name)
        
    def update_color_map(self):
        self.color_map.clear()
        for n in self.nodes:
            if self.nodes[n].get('color'):
                self.color_map.append(self.nodes[n]['color'])
            else:
                self.color_map.append(self._DEFAULT_COLOR)
            
    def set_node_color(self, node, color):
        self.graph.nodes[node]['color'] = color
        
    def replace_node(self, node, to_graph):
        print(node)
        print(self.graph.nodes)
        node_data = self.graph.nodes[node]
        print(node_data)
        self.delete_node(node)
        
        if node in to_graph.nodes:
           return

        to_graph.graph.add_nodes_from([
            (node, node_data)
        ])
        
    def get_node_info(self, node):
        info = ""
        info += f"Node {node}\n"
        for k, v in self.graph.nodes[node].items():
            info +=  f"{k} is {v}\n"
        return info
    
    def delete_edge(self, edge):
        self.graph.remove_edge(*edge)
        
    def set_edge_color(self, edge, color):
        self.graph[edge[0]][edge[1]]['color'] = color
        
    def get_edge_info(self, edge):
        info = ""
        info += f"Edge {edge[0]}->{edge[1]}\n"
        for k, v in self.graph.edges[edge[0], edge[1]].items():
            info +=  f"{k} is {v}\n"
        return info
    
    def to_full_graph(self):
        nodes = self.nodes
        nodes_data = dict(self.graph.nodes.data())
        full_graph = nx.complete_graph(nodes, nx.DiGraph())
        
        full_graph.graph['name'] = self.name
        for n in full_graph.nodes:
            if nodes_data[n]:
                for key, value in nodes_data[n].items():
                    full_graph.nodes[n][key] = value
            
        self.graph = full_graph
        self.is_full = True
        return True
    
    def find_eulerian_cycle(self):
        try:
            path = list(nx.eulerian_path(self.graph))
            if path[0][0] == path[-1][1]:
                return path
            return False
        except Exception as e:
            return False
        
    def get_all_routes(self, source, target):
        res = "all paths:\n"
        all_paths = nx.all_simple_paths(self.graph, source=source, target=target)
        
        for path in all_paths:    
            res += str(path)
        
        try:
            shortest_path = list(nx.shortest_path(self.graph, source=source, target=target))
        except Exception as e:
            return "\nNO routes!"
        shortest_path_length = nx.shortest_path_length(self.graph, source=source, target=target)
        res += f"\n\nshortest path: {shortest_path}\nand it's length is {shortest_path_length}"
            
        return res
    
    def show_subgraph(self, nodes):
        subgraph = self.graph.subgraph(nodes)
        
        plt.figure(self.name+" subgraph")
        nx.draw(subgraph, with_labels=True, font_weight='bold')
        plt.show()
        
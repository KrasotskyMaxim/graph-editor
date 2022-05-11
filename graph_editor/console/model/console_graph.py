import networkx as nx
import matplotlib.pyplot as plt

from graph_editor.console.model.graph_errors import *


class ConsoleGraph:
    _path_to_save = './graph_editor/saved_graphs/'
    _type_edges = ['--', '<-', '->']
    _DEFAULT_COLOR = 'blue'
    
    def __init__(self, *args, **kwargs):
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
                    edge = tuple(e.split(type_e))
                    break
            if edge:
                self.graph.add_edge(*edge)
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
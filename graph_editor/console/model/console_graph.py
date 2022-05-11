import networkx as nx

from graph_editor.console.model.graph_errors import *


class ConsoleGraph:
    _path_to_save = './graph_editor/saved_graphs/'
    _type_edges = ['--', '<-', '->']
    
    def __init__(self, *args, **kwargs):
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
        for d in node_data:
            self.set_node_data(node=node_name, data=node_data)
        return True
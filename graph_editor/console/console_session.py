from distutils.log import warn
import sys, os, time, re

from graph_editor.console.model.console_graph import ConsoleGraph


# TODO: - Является ли граф полным


class ConsoleSession:
    _start_commands = {
        'create graph': '1',
        'load graph': '2',
        'select graph': '3',
        'show graphs': '4',
        'exit': '0'
    }
    _graph_commands = {
        'node settings': '1',
        'edge settings': '2',
        'info': '3',
        'save': '4',
        'special functions': '5',
        'show in label': '6',
        'exit': '0'
    }
    _node_commands = {
        'add node': '1',
        'select node': '2',
        'show nodes': '3',
        'exit': '0'
    }
    _single_node_commands = {
        'delete node': '1',
        'set node data': '2',
        'set node color': '3',
        'show node info': '4',
        'replace node': '5',
        'exit': '0'
    }
    _edge_commands = {
        'add edge': '1',
        'select edge': '2',
        'show edges': '3',
        'exit': '0'
    }
    _single_edge_commands = {
        'delete edge': '1',
        'set edge color': '2',
        'show edge info': '3',
        'exit': '0'
    }
    _special_fucntions_comamnds = {
        'to full graph': '1',
        'find eulerian cycle': '2',
        'find all routes': '3',
        'find subgraph': '4',
        'exit': '0'
    }
    
    
    def __init__(self, *args, **kwargs):
        self.graphs = []
        self.current_graph = None
        self.current_edge = None
        self.current_node = None 
        if kwargs.get('load'):
            self.load_graph(path=kwargs['load'])
        
    def start_main_session(self):
        self.show_start_menu()
        
        
    def show_start_menu(self, warning=None):
        self.clear_console()
        if warning:
            print(warning, end='\n\n')
        print("START MENU:")
        print("1 - Create graph")
        print("2 - Load graph")
        print("3 - Select graph")
        print("4 - Show graphs")
        print("0 - Exit")
        command = input("Enter: ")
        self.parse_start_menu(command=command)
        
    def show_graph_menu(self, warning=None):
        self.clear_console()
        if warning:
            print(warning, end='\n\n')
        print("GRAPH MENU")
        print("1 - Node settings")
        print("2 - Edge settings")
        print("3 - Info")
        print("4 - Save")
        print("5 - Special functions")
        print("6 - Show in label")
        print("0 - Exit")
        command = input("Enter: ")
        self.parse_graph_menu(command=command)
        
    def show_node_menu(self, warning=None):
        self.clear_console()
        if warning:
            print(warning, end='\n\n')
        print("NODE MENU")
        print("1 - Create node")
        print("2 - Select node")                
        print("3 - Show nodes")
        print("0 - exit")
        command = input("Enter: ")
        self.parse_node_menu(command=command)
        
    def show_single_node_menu(self, warning=None, node_name=None):
        self.clear_console()
        if warning:
            print(warning, end='\n\n')
        print(f"NODE '{self.current_node}' MENU")
        print("1 - Delete node")
        print("2 - Set node data")
        print("3 - Set node color")
        print("4 - Show node info")
        print("5 - Replace node")
        print("0 - exit")
        command = input("Enter: ")
        self.parse_single_node_menu(command=command, node_name=node_name)
        
    def show_edge_menu(self, warning=None):
        self.clear_console()
        if warning:
            print(warning, end='\n\n')
        print("EDGE MENU")
        print("1 - Add edge")
        print("2 - Select edge")
        print("3 - Show edges")
        print("0 - exit")
        command = input("Enter: ")
        self.parse_edge_menu(command=command)
        
    def show_single_edge_menu(self, warning=None, edge=None):
        self.clear_console()
        if warning:
            print(warning, end='\n\n')
        print(f"EDGE FROM '{self.current_edge[0]}' TO '{self.current_edge[1]}' MENU")
        print("1 - Delete edge")
        print("2 - Set edge color")
        print("3 - Show edge info")
        print("0 - exit")
        command = input("Enter: ")
        self.parse_single_edge_menu(command=command, edge=edge)
             
    def show_special_functions_menu(self, warning=None):
        self.clear_console()
        if warning:
            print(warning, end='\n\n')
        print("1 - To full graph")
        print("2 - Find eulerian cycle")
        print("3 - Find all routes")
        print("4 - Find subgraph")
        print("0 - exit")
        command = input("Enter: ")
        self.parse_special_functions_menu(command=command)
        
        
    def parse_start_menu(self, command):
        if command == self._start_commands['create graph']:
            self.create_graph()
        elif command == self._start_commands['load graph']:
            self.load_graph()
        elif command == self._start_commands['select graph']:
            self.select_graph()
        elif command == self._start_commands['show graphs']:
            self.show_graphs()
        elif command == self._start_commands['exit']:
            self.end_main_session()
        else:
            self.show_start_menu("Incorrect start command!")
            
    def parse_graph_menu(self, command):
        if command == self._graph_commands['node settings']:
            self.show_node_menu()
        elif command == self._graph_commands['edge settings']:
            self.show_edge_menu()
        elif command == self._graph_commands['info']:
            self.show_graph_info()
        elif command == self._graph_commands['save']:
            self.save_graph()
        elif command == self._graph_commands['special functions']:
            self.show_special_functions_menu()
        elif command == self._graph_commands['show in label']:
            self.show_graph_in_label()
        elif command == self._graph_commands['exit']:
            self.end_graph_session()
        else:
            self.show_graph_menu("Incorrect graph command!")
            
    def parse_node_menu(self, command):
        if command == self._node_commands['add node']:
            self.add_node()
        elif command == self._node_commands['select node']:
            self.select_node()
        elif command == self._node_commands['show nodes']:
            self.show_nodes()
        elif command == self._node_commands['exit']:
            self.end_node_session()
        else:
            self.show_node_menu("Incorrect node command!")
            
    def parse_single_node_menu(self, command, node_name=None):
        if command == self._single_node_commands['delete node']:
            self.delete_node(self.current_node)
        elif command == self._single_node_commands['set node data']:
            self.set_node_data()
        elif command == self._single_node_commands['set node color']:
            self.set_node_color()
        elif command == self._single_node_commands['replace node']:
            self.replace_node(self.current_node)
        elif command == self._single_node_commands['show node info']:
            self.show_node_info(self.current_node)
        elif command == self._single_node_commands['exit']:
            self.end_single_node_session()
        else:
            self.show_single_node_menu("Incorrect single node command!", node_name) 
    
    def parse_edge_menu(self, command):
        if command == self._edge_commands['add edge']:
            self.add_edge()
        elif command == self._edge_commands['select edge']:
            self.select_edge()
        elif command == self._edge_commands['show edges']:
            self.show_edges()
        elif command == self._edge_commands['exit']:
            self.end_edge_session()
        else:
            self.show_edge_menu("Incorrect node command!")
    
    def parse_single_edge_menu(self, command, edge=None):
        if command == self._single_edge_commands['delete edge']:
            self.delete_edge()
        elif command == self._single_edge_commands['set edge color']:
            self.set_edge_color()
        elif command == self._single_edge_commands['show edge info']:
            self.show_edge_info()
        elif command == self._single_edge_commands['exit']:
            self.end_single_edge_session(edge=edge)
        else:
            self.show_single_edge_menu("Incorrect single edge command!", edge) 
    
    def parse_special_functions_menu(self, command):
        if command == self._special_fucntions_comamnds['to full graph']:
            self.to_full_graph()
        elif command == self._special_fucntions_comamnds['find eulerian cycle']:
            self.find_eulerian_cycle()
        elif command == self._special_fucntions_comamnds['find all routes']:
            self.find_all_routes()
        elif command == self._special_fucntions_comamnds['find subgraph']:
            self.find_subgraph()
        elif command == self._single_edge_commands['exit']:
            self.end_special_functions_session()
        else:
            self.show_special_functions__menu("Incorrect special functions command!")      
            
            
    def create_graph(self):
        self.clear_console()
        print("Create NEW graph\n")
        graph_name = input("graph name: ")
        nodes = input("nodes: ") # A B C 1 2 3
        edges = input("edges: ") # A->B B->B 1--2 2<-3
        
        graph = ConsoleGraph(
            name=graph_name,
            nodes=nodes,
            edges=edges
        )
        self.graphs.append(graph)
        self.current_graph = graph
        self.show_graph_menu(warning="Graph create succesfully!")
        
    def show_graph_info(self):
        self.clear_console()
        print(self.current_graph.info)
        time.sleep(5)
        self.show_graph_menu()

    def show_graphs(self):
        self.clear_console()
        if not self.graphs:
            print("No graphs!")
        else:
            for i, g in enumerate(self.graphs):
                print(f'{i+1}) {g.name}')
        time.sleep(5)
        self.show_start_menu()
        
    def show_graph_in_label(self):
        self.current_graph.show_in_label()
        self.show_graph_menu()

    def load_graph(self, path=None):
        if not path:
            path = input("file path: ")
        
        graph = ConsoleGraph()
        self.current_graph = graph
        load_graph = self.current_graph.load_from_gml(path=path)
        if self.check_exists_graphs(graph_name=load_graph):
            self.graphs.append(graph)
            self.show_graph_menu("Graph load succesfully!")
        else:
            self.show_start_menu(warning="This graph already exists!")
        
    def save_graph(self, path=None):
        if not path:
            path = input("File name: ")
        if self.current_graph.save_to_gml(path=path):
            self.show_graph_menu(warning="Graph saved succesfully!")
        
    def select_graph(self, graph_name=None):
        if not graph_name:
            graph_name = input("graph name: ")
        
        flag = False
        for g in self.graphs:
            if g.name == graph_name:
                self.current_graph = g
                flag = True
                break
        if not flag:
            self.show_start_menu(warning="Doesn't have this graph name!")   
        self.show_graph_menu()
        
    def check_exists_graphs(self, graph_name=None):
        if not graph_name:
            return False
        
        for g in self.graphs:
            if graph_name == g.name:
                return False
        return True
            
            
    def add_node(self, node_name=None, data=None):
        if not node_name:
            node_name = input("node name: ")
            pass 
        
        if not data:
            data = input("data key--data value: ") # name--Alex
            # data = data.split()
            for d in data:
                self.validate_node_data(d)
                
        self.current_graph.add_node(node_name=node_name, node_data=data)
        self.show_node_menu(warning="Create new node!")
        
    def validate_node_data(self, data):
        # pattern = r'.+--.+'
        # if not re.match(pattern, data):
        #     self.show_node_menu(warning="Incorrect input data!")
        # else:
        #     return True
        return True
        
    def set_node_data(self, node=None, data=None):
        if not node:
            node = input("node name: ")
            if node not in self.current_graph.nodes:
                self.show_node_menu(warning="This node doesn't exists!")
                return 
        
        if not data:
            data = input("data key--data value: ") # name--Alex
            self.validate_node_data(data)
            
        if self.current_graph.set_node_data(node=node, data=data):
            self.show_single_node_menu(warning="Node data successful added!")
            
    def select_node(self, node_name=None):
        if not node_name:
            node_name = input("node name: ")
        
        self.current_node = node_name
        self.show_single_node_menu(node_name=self.current_node)
        
    def delete_node(self, node_name=None):
        for_delete = self.current_node
        self.current_node = None 
        self.current_graph.delete_node(for_delete)
        self.show_node_menu(warning=f"Node {node_name} successful deleted!")
            
    def set_node_color(self, node_name=None, node_color=None):
        if not node_color:
            node_color = input("node color: ")
            
        self.current_graph.set_node_color(node=self.current_node, color=node_color)
        self.show_single_node_menu(warning="Node color successful changed!")
    
    def replace_node(self, node_name=None, to_graph=None):
        if not to_graph:
            flag = False
            while not flag:
                to_graph = input("to graph: ")
                for g in self.graphs:
                    if to_graph == g.name:
                        to_graph = g
                        flag = True
                        break
            
        self.current_graph.replace_node(node_name, to_graph)
        self.show_single_node_menu(warning=f"Node moved to {to_graph.name}")
    
    def show_node_info(self, node_name=None):
        info = self.current_graph.get_node_info(self.current_node)
        self.clear_console()
        print(info)
        time.sleep(5)
        self.show_single_node_menu()

            
    def show_nodes(self):
        self.clear_console()
        nodes = self.current_graph.nodes
        for i, n in enumerate(nodes):
            print(i+1, ') ', n)
        time.sleep(5)
        self.show_node_menu()
    
    def show_edges(self):
        self.clear_console()
        edges = self.current_graph.edges
        for i, e in enumerate(edges):
            print(f"{i+1}) from {e[0]} to {e[1]}")
        time.sleep(5)
        self.show_edge_menu()
            
    def add_edge(self, edge=None):
        if not edge:
            edge = input("edge: ")
        
        self.current_graph.parse_edges(edges=edge)
        self.show_edge_menu(warning="Edge successful added!")
        
    def select_edge(self, start=None, end=None):
        if not start:
            start = input("start node: ")
        if not end:
            end = input("end node: ")
            
        self.current_edge = (start, end)
        self.show_single_edge_menu(edge=(start, end))
        
    def delete_edge(self):
        self.current_graph.delete_edge(self.current_edge)
        self.show_edge_menu(warning="Edge delete succesfully!")
        
    def set_edge_color(self, color=None):
        if not color:
            color = input("color: ")
        
        self.current_graph.set_edge_color(self.current_edge, color)
        self.show_single_edge_menu(warning="Set color successful!")
        
    def show_edge_info(self):
        info = self.current_graph.get_edge_info(self.current_edge)
        self.clear_console()
        print(info)
        time.sleep(5)
        self.show_single_edge_menu()
            
    def to_full_graph(self):
        print("to full graph!")
        
    def find_eulerian_cycle(self):
        print("find eulerian cycle!")
        
    def find_all_routes(self):
        print("find all routes!")
        
    def find_subgraph(self):
        print("find subgraph!")
    
            
    def end_node_session(self):
        self.show_graph_menu()
        
    def end_edge_session(self):
        self.show_graph_menu()
            
    def end_graph_session(self):
        self.show_start_menu()
        
    def end_main_session(self):
        self.clear_console()
        sys.exit()
        
    def end_single_node_session(self):
        self.show_node_menu()
        
    def end_single_edge_session(self, edge):
        self.show_edge_menu(edge)
        
    def end_special_functions_session(self):
        self.show_graph_menu()
        
    @staticmethod
    def clear_console():
        os.system("CLS")
        
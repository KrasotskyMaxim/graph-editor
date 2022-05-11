from graph_editor.console.controller.console_session_parser import ConsoleSessionParses

import os, time


class ConsoleSessionView:
    def __init__(self, parser_session):
        self.parser = ConsoleSessionParses(session=parser_session)
        
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
        'set node type': '3',
        'set node color': '4',
        'replace node': '5',
        'show node info': '6',
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
        self.parser.parse_start_menu(command=command)
        
    def show_graph_menu(self, warning=None):
        self.clear_console()
        if warning:
            print(warning, end='\n\n')
        print("GRAPH MENU")
        print("1 - Node settings")
        print("2 - Edge settings")
        print("3 - info")
        print("4 - save")
        print("5 - special functions")
        print("0 - exit")
        command = input("Enter: ")
        self.parser.parse_graph_menu(command=command)
        
    def show_node_menu(self, warning=None):
        self.clear_console()
        if warning:
            print(warning, end='\n\n')
        print("1 - Create node")
        print("2 - Select node")                
        print("4 - Show nodes")
        print("0 - exit")
        command = input("Enter: ")
        self.parser.parse_node_menu(command=command)
        
    def show_single_node_menu(self, warning=None):
        self.clear_console()
        if warning:
            print(warning, end='\n\n')
        print("1 - Delete node")
        print("2 - Set node data")
        print("3 - Set node type")
        print("4 - Set node color")
        print("5 - Show node info")
        print("6 - Replace node")
        print("0 - exit")
        command = input("Enter: ")
        self.parser.parse_single_node_menu(command=command)
        
    def show_edge_menu(self, warning=None):
        self.clear_console()
        if warning:
            print(warning, end='\n\n')
        print("1 - Add edge")
        print("2 - Select edge")
        print("3 - Show edges")
        print("0 - exit")
        command = input("Enter: ")
        self.parser.parse_edge_menu(command=command)
        
    def show_single_edge_menu(self, warning=None):
        self.clear_console()
        if warning:
            print(warning, end='\n\n')
        print("1 - Delete edge")
        print("2 - Set edge type")
        print("3 - Show edge info")
        print("0 - exit")
        command = input("Enter: ")
        self.parser.parse_single_edge_menu(command=command)
             
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
        self.parser.parse_special_functions_menu(command=command)
    
    def show_graph_info(self, graph):
        self.clear_console()
        print(graph.info)
        time.sleep(5)
        self.show_graph_menu()
    
    def show_new_graph_menu(self, warning):
        self.clear_console()
        print("Create NEW graph\n")
        if warning:
            print(warning, end='\n\n')
        graph_name = input("graph name: ")
        nodes = input("nodes: ") # A B C 1 2 3
        edges = input("edges: ") # A->B B->B 1--2 2<-3
        self.parser.parse_new_graph(name=graph_name, nodes=nodes, edges=edges)
    
    @staticmethod
    def clear_console():
        os.system("CLS")
    
    
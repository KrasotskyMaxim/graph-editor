from graph_editor.console.console_session import ConsoleSession


class ConsoleSessionParses:
    def __init__(self, session):
        self.session = session
        
    def parse_start_menu(self, command):
        if command == self._start_commands['create graph']:
            self.console.create_graph()
        elif command == self._start_commands['load graph']:
            self.console.load_graph()
        elif command == self._start_commands['select graph']:
            self.console.select_graph()
        elif command == self._start_commands['show graphs']:
            self.console.show_graphs()
        elif command == self._start_commands['exit']:
            self.console.end_main_session()
        else:
            self.console.show_start_menu("Incorrect start command!")
            
    def parse_graph_menu(self, command):
        if command == self._graph_commands['node settings']:
            self.console.show_node_menu()
        elif command == self._graph_commands['edge settings']:
            self.console.show_edge_settings_menu()
        elif command == self._graph_commands['info']:
            self.console.show_graph_info()
        elif command == self._graph_commands['save']:
            self.console.save_graph()
        elif command == self._graph_commands['special functions']:
            self.console.show_special_functions_menu()
        elif command == self._graph_commands['exit']:
            self.console.end_graph_session()
        else:
            self.console.show_graph_menu("Incorrect graph command!")
            
    def parse_node_menu(self, command):
        if command == self._node_commands['add node']:
            self.console.add_node()
        elif command == self._node_commands['delete node']:
            self.console.delete_node()
        elif command == self._node_commands['set node data']:
            self.console.set_node_data()
        elif command == self._node_commands['replace node']:
            self.console.replace_node
        elif command == self._node_commands['exit']:
            self.console.end_node_session()
        else:
            self.console.show_node_menu("Incorrect node command!")
            
    def parse_single_node_menu(self, command):
        pass 
    
    def parse_edge_menu(self, command):
        pass
    
    def parse_single_edge_menu(self, command):
        pass 
    
    def parse_special_functions_menu(self, command):
        pass 
    
    def parse_new_graph(self, **kwargs):
        self.session
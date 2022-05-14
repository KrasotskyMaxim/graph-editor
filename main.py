
from user_input.cmd_input import parse_args, set_args

from graph_editor.console.console_session import ConsoleSession

from sys import argv



if __name__ == "__main__":
    args = parse_args(argv[1:])
    settings = set_args(args)
    
    session = ConsoleSession(settings)
    session.start_session("start menu")
    
  
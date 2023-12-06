from module.InputScanner import InputScanner
from module.OutputPrinter import OutputPrinter
from module.static.dedicated_configuration.MenuFunctions import MenuFunctions

# Class which specifies how the Menu class instance should behave
class MenuConfiguration:
    options_and_functions = {
        '1': MenuFunctions.print_all_users,
        '2': MenuFunctions.print_all_posts,
        '3': MenuFunctions.print_all_comments,
        '0': MenuFunctions.exit_program
    }

    options_and_descriptions = {
        '1': 'Print Users',
        '2': 'Print Posts',
        '3': 'Print Comments',
        '0': 'Exit'
    }

    options_and_conditions = {
        '1': lambda: True,
        '2': lambda: True,
        '3': lambda: True,
        '0': lambda: True
    }

    scanner = InputScanner(OutputPrinter)

    printer = OutputPrinter


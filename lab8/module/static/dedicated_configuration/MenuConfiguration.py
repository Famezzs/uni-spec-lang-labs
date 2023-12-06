from module.InputScanner import InputScanner
from module.OutputPrinter import OutputPrinter
from module.static.dedicated_configuration.MenuFunctions import MenuFunctions

# Class which specifies how the Menu class instance should behave
class MenuConfiguration:
    options_and_functions = {
        '1': MenuFunctions.generate_csv_file,
        '2': MenuFunctions.plot,
        '3': MenuFunctions.histogram,
        '4': MenuFunctions.plot_and_histogram,
        '0': MenuFunctions.exit_program
    }

    options_and_descriptions = {
        '1': 'Generate CSV File',
        '2': 'Plot',
        '3': 'Histogram',
        '4': 'Plot and Histogram',
        '0': 'Exit'
    }

    options_and_conditions = {
        '1': lambda: True,
        '2': lambda: True,
        '3': lambda: True,
        '4': lambda: True,
        '0': lambda: True
    }

    scanner = InputScanner(OutputPrinter)

    printer = OutputPrinter


from data.shared.classes.InputScanner import InputScanner
from data.shared.classes.OutputPrinter import OutputPrinter
from data.shared.configuration.MenuFunctions import MenuFunctions

# Class which specifies how the Menu class instance should behave
class MenuConfiguration:
    options_and_functions = {
        '1': MenuFunctions.text_to_art_library,
        '2': MenuFunctions.display_fonts,
        '3': MenuFunctions.text_to_art_own,
        '4': MenuFunctions.draw_figure, 
        '5': MenuFunctions.perform_calculation,
        '6': MenuFunctions.display_calculator_logs,
        '7': MenuFunctions.load_calculator_logs,
        '8': MenuFunctions.print_all_users,
        '9': MenuFunctions.print_all_posts,
        '10': MenuFunctions.print_all_comments,
        '11': MenuFunctions.generate_csv_file,
        '12': MenuFunctions.plot,
        '13': MenuFunctions.histogram,
        '14': MenuFunctions.plot_and_histogram,
        '0': MenuFunctions.exit_program
    }

    options_and_descriptions = {
        '1': 'Text to art (library)',
        '2': 'Show fonts',
        '3': 'Text to art (own implementation)',
        '4': 'Draw Figure',
        '5': 'Perform calculation',
        '6': 'Display calculation logs',
        '7': 'Load calculation logs',
        '8': 'Print Users',
        '9': 'Print Posts',
        '10': 'Print Comments',
        '11': 'Generate CSV File',
        '12': 'Plot',
        '13': 'Histogram',
        '14': 'Plot and Histogram',
        '0': 'Exit'
    }

    scanner = InputScanner(OutputPrinter)

    printer = OutputPrinter


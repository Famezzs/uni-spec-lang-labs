import os
from data.shared.abstract.ClearsConsole import ClearsConsole
from termcolor import colored
from tabulate import tabulate


class OutputPrinter(ClearsConsole):
    """
    A class for handling various types of output printing in the application.

    This class provides static methods to print text and tables to the console, with options for colored output 
    and controlling newline behavior.

    Methods:
        print(output_string, additional_next_line=False, no_new_line=False): Prints the given string to the console.
        print_colored(output_string, color, additional_next_line=False): Prints the given string in color to the console.
        print_as_table(data: list, additional_next_line=False): Prints the given data as a table.
        print_as_colored_table(data: list, color, additional_next_line=False): Prints the given data as a colored table.
        clear_console(): Clears the console screen.
    """

    @staticmethod
    def print(output_string, additional_next_line=False, no_new_line=False):
        """
        Prints the given string to the console. 

        Args:
            output_string (str): The string to be printed.
            additional_next_line (bool, optional): Adds an additional newline after the output if True. Defaults to False.
            no_new_line (bool, optional): Omits the trailing newline if True. Defaults to False.
        """
        if no_new_line:
            print(output_string, end='')
        else:
            print(output_string)
        if additional_next_line:
            print()

    @staticmethod
    def print_colored(output_string, color, additional_next_line=False):
        """
        Prints the given string in color to the console.

        Args:
            output_string (str): The string to be printed.
            color (str): The color to print the string in.
            additional_next_line (bool, optional): Adds an additional newline after the output if True. Defaults to False.
        """
        print(colored(output_string, color))
        if additional_next_line:
            print()

    @staticmethod
    def print_as_table(data: list, additional_next_line=False):
        """
        Prints the given data as a table.

        Args:
            data (list): The data to be printed as a table.
            additional_next_line (bool, optional): Adds an additional newline after the table if True. Defaults to False.
        """
        print(tabulate(data, headers="keys"))
        if additional_next_line:
            print()

    @staticmethod
    def print_as_colored_table(data: list, color, additional_next_line=False):
        """
        Prints the given data as a colored table.

        Args:
            data (list): The data to be printed as a table.
            color (str): The color to print the table in.
            additional_next_line (bool, optional): Adds an additional newline after the table if True. Defaults to False.
        """
        print(colored(tabulate(data, headers="keys"), color))
        if additional_next_line:
            print()

    @staticmethod
    def clear_console():
        """
        Clears the console screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

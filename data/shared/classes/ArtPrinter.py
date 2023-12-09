__all__ = ['ArtPrinter']
from data.shared.exception.InvalidColor import InvalidColor
from termcolor import colored


class ArtPrinter:
    """
    A utility class for printing ASCII art.

    Provides static methods to print ASCII art in the console, with options to print in plain text or 
    with a specified color using the termcolor library.

    Methods:
        print(output_string): Prints the given ASCII art in plain text.
        colored_print(output_string, color): Prints the ASCII art in the specified color.
    """

    @staticmethod
    def print(output_string):
        """
        Prints the given ASCII art as plain text.

        Args:
            output_string (str): The ASCII art to be printed.
        """
        print()
        print(output_string)
        print()

    @staticmethod
    def colored_print(output_string, color):
        """
        Prints the ASCII art in the specified color using the termcolor library.

        Args:
            output_string (str): The ASCII art to be printed.
            color (str): The color in which the ASCII art should be printed.

        Raises:
            InvalidColor: If the specified color is not supported or invalid.
        """
        print()
        try:
            print(colored(output_string, color))
        except:
            raise InvalidColor('Invalid color provided')
        print()

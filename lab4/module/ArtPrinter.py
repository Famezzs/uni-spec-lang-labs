from module.abstract.Printer import Printer
from module.exception.InvalidColor import InvalidColor
from termcolor import colored

class ArtPrinter(Printer):
    @staticmethod
    def print(output_string):
        print()
        print(output_string)
        print()
    
    @staticmethod
    def colored_print(output_string, color):
        print()
        try:
            print(colored(output_string, color))
        except:
            raise InvalidColor('Invalid color provided')
        print()
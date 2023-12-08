from data.shared.exception.InvalidColor import InvalidColor
from termcolor import colored

class ArtPrinter:
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
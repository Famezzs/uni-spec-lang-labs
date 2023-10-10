from module.InputScanner import InputScanner
from module.ArtGenerator import ArtGenerator
from module.Menu import Menu
from module.ArtPrinter import ArtPrinter

class MenuFunctions:
    @staticmethod
    def text_to_art():
        text = InputScanner.scan('Text to transform: ')
        font = InputScanner.scan('Font (leave blank for default): ', allow_empty=True)
        color = InputScanner.scan('Color (leave blank for default): ', allow_empty=True)

        if InputScanner.input_empty(font) == True:
            font = ArtGenerator.default_font    
        if InputScanner.input_empty(color) == True:
            ArtPrinter.print(ArtGenerator.text_to_art(text=text, font=font))
        else:
            ArtPrinter.colored_print(ArtGenerator.text_to_art(text=text, font=font), color)

    @staticmethod
    def display_fonts():
        print('Available fonts:')
        ArtPrinter.print(ArtGenerator.get_fonts())

    @staticmethod
    def exit_programme():
        exit(0)

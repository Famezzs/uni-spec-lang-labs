from module.InputScanner import InputScanner
from module.ArtGenerator import ArtGenerator
from module.ArtPrinter import ArtPrinter

class MenuFunctions:
    @staticmethod
    def save_to_file(content):
        path = InputScanner.scan('Specify path to the file: ')
        file = open(path, 'a')
        file.write(content)
        file.close()

    @staticmethod
    def text_to_art():
        text = InputScanner.scan('Text to transform: ')
        font = InputScanner.scan('Font (leave blank for default): ', allow_empty=True)
        color = InputScanner.scan('Color (leave blank for default): ', allow_empty=True)

        if InputScanner.input_empty(font) == True:
            font = ArtGenerator.default_font    

        result = ArtGenerator.text_to_art(text=text, font=font)
        if InputScanner.input_empty(color) == True:
            ArtPrinter.print(result)
        else:
            ArtPrinter.colored_print(result, color)
        
        option = InputScanner.scan('Save to file? (Y/N): ')
        if option.startswith('y'):
            MenuFunctions.save_to_file(result)

    @staticmethod
    def display_fonts():
        print('Available fonts:')
        ArtPrinter.print(ArtGenerator.get_fonts())

    @staticmethod
    def exit_programme():
        exit(0)

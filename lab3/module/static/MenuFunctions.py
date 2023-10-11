from module.InputScanner import InputScanner
from module.ArtGenerator import ArtGenerator
from module.ArtPrinter import ArtPrinter
from module.ArtScaler import ArtScaler

class MenuFunctions:
    @staticmethod
    def print_art(result, color):
        if InputScanner.input_empty(color) == True:
            ArtPrinter.print(result)
        else:
            ArtPrinter.colored_print(result, color)

    @staticmethod
    def save_to_file(content):
        path = InputScanner.scan('Specify path to the file: ')
        file = open(path, 'a')
        file.write(content)
        file.close()

    @staticmethod
    def scale_art(content):
        multiplier = InputScanner.scan('Specify integer multiplier: ')
        return ArtScaler.scale(int(multiplier), content)    

    @staticmethod
    def text_to_art():
        text = InputScanner.scan('Text to transform: ')
        font = InputScanner.scan('Font (leave blank for default): ', allow_empty=True)
        color = InputScanner.scan('Color (leave blank for default): ', allow_empty=True)

        if InputScanner.input_empty(font) == True:
            font = ArtGenerator.default_font    

        result = ArtGenerator.text_to_art(text=text, font=font)
        MenuFunctions.print_art(result, color)
        
        option = InputScanner.scan('Scale art? (Y/N): ')
        if option.startswith('y'):
            result = MenuFunctions.scale_art(result)
            MenuFunctions.print_art(result, color)

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

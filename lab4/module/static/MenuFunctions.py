from module.InputScanner import InputScanner
from module.ArtGenerator import ArtGenerator
from module.ArtPrinter import ArtPrinter
from module.ArtScaler import ArtScaler
from module.static.ArtGeneratorConfiguration import ArtGeneratorConfiguration

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
        character = InputScanner.scan('Base character (leave blank for default): ', allow_empty=True)
        color = InputScanner.scan('Color (leave blank for default): ', allow_empty=True)

        art_generator = ArtGenerator(ArtGeneratorConfiguration.letters_and_art, ArtGeneratorConfiguration.elements_in_letter_array, ArtGeneratorConfiguration.default_symbol)

        result = art_generator.text_to_art(text, character)
        MenuFunctions.print_art(result, color)
        
        option = InputScanner.scan('Scale art? (Y/N): ')
        if option.startswith('y'):
            result = MenuFunctions.scale_art(result)
            MenuFunctions.print_art(result, color)

        option = InputScanner.scan('Save to file? (Y/N): ')
        if option.startswith('y'):
            MenuFunctions.save_to_file(result)

    @staticmethod
    def exit_programme():
        exit(0)

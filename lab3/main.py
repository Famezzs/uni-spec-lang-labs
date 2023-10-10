from module.InputScanner import InputScanner
from module.ArtGenerator import ArtGenerator
from module.Menu import Menu
from module.ArtPrinter import ArtPrinter
from module.exception.InvalidOption import InvalidOption
from module.exception.InvalidColor import InvalidColor

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

def display_fonts():
    print('Available fonts:')
    ArtPrinter.print(ArtGenerator.get_fonts())

def exit_programme():
    exit(0)

options_and_functions = {
    '1': text_to_art,
    '2': display_fonts,
    '0': exit_programme
}

options_and_descriptions = {
    '1': 'Text to art',
    '2': 'Show fonts',
    '0': 'Exit'
}

def main():
    menu = Menu(options_and_descriptions, options_and_functions)

    while True:
        menu.print_menu()
        option = InputScanner.scan('Choose one option: ')
        try:
            menu.invoke_function(option)
        except InvalidOption:
            pass
        except InvalidColor:
            print('Wrong color specified')

main()
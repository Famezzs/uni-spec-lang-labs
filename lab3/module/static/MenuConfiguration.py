from module.static.MenuFunctions import MenuFunctions

class MenuConfiguration:
    options_and_functions = {
        '1': MenuFunctions.text_to_art,
        '2': MenuFunctions.display_fonts,
        '0': MenuFunctions.exit_programme
    }

    options_and_descriptions = {
        '1': 'Text to art',
        '2': 'Show fonts',
        '0': 'Exit'
    }
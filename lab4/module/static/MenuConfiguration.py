from module.static.MenuFunctions import MenuFunctions

class MenuConfiguration:
    options_and_functions = {
        '1': MenuFunctions.text_to_art,
        '0': MenuFunctions.exit_programme
    }

    options_and_descriptions = {
        '1': 'Text to art',
        '0': 'Exit'
    }
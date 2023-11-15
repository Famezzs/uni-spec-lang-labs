from module.static.MenuFunctions import MenuFunctions

class MenuConfiguration:
    options_and_functions = {
        '1': MenuFunctions.draw_figure,
        '0': MenuFunctions.exit_programme
    }

    options_and_descriptions = {
        '1': 'Draw Figure',
        '0': 'Exit'
    }
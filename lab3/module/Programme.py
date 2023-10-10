from module.Menu import Menu
from module.InputScanner import InputScanner
from module.exception.ExceptionHandler import ExceptionHandler
from module.static.MenuConfiguration import MenuConfiguration

class Programme:
    def run(self):
        menu = Menu(MenuConfiguration.options_and_descriptions, MenuConfiguration.options_and_functions)

        while True:
            menu.print_menu()
            option = InputScanner.scan('Choose one option: ')
            try:
                menu.invoke_function(option)
            except Exception as exception:
                ExceptionHandler.handle(exception)
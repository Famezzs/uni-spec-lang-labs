from data.shared.abstract.ClearsConsole import ClearsConsole
from data.shared.exception.InvalidOption import InvalidOption

# Class which is used for rendering the appliaction's menu
class Menu(ClearsConsole):
    def __init__(self, configuration):
        self.configuration = configuration
        self.options_and_descriptions = configuration.menu_configuration.options_and_descriptions
        self.options_and_functions = configuration.menu_configuration.options_and_functions
        self.scanner = configuration.menu_configuration.scanner
        self.printer = configuration.menu_configuration.printer

    def __handle_not_present_option(self):
        raise InvalidOption('Invalid option specified')

    def option_present(self, option):
        return option in self.options_and_functions

    def invoke_function(self, option):
        if self.option_present(option) == False:
            self.__handle_not_present_option()
        self.options_and_functions[option]()
    
    def print_menu(self):
        self.printer.clear_console()
        for option in list(self.options_and_descriptions.keys()):
            if option == '0':
                self.printer.print('')
            self.printer.print('[' + option + '] - ' + self.options_and_descriptions[option])
        self.printer.print('')

    def scan_and_invoke_option(self):
        option = self.scanner.scan()
        self.printer.clear_console()
        self.invoke_function(option)
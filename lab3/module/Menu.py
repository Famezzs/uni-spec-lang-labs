from module.exception.InvalidOption import InvalidOption

class Menu:
    def __init__(self, options_and_descriptions, options_and_functions):
        self.options_and_descriptions = options_and_descriptions
        self.options_and_functions = options_and_functions

    def option_present(self, option):
        return option in self.options_and_functions

    def invoke_function(self, option):
        if self.option_present(option) == True:
            self.options_and_functions[option]()
        else:
            raise InvalidOption()
    
    def print_menu(self):
        print()
        for option in list(self.options_and_descriptions.keys()):
            print('[', option, '] - ', self.options_and_descriptions[option])
        print()
    
from data.shared.abstract.ClearsConsole import ClearsConsole
from data.shared.exception.InvalidOption import InvalidOption


class Menu(ClearsConsole):
    """
    A class for rendering and managing the application's menu.

    This class provides functionality to display a menu, scan user input for menu options, 
    and invoke the corresponding functions based on the user's choice.

    Attributes:
        configuration: The configuration object containing menu settings.
        options_and_descriptions (dict): A dictionary mapping options to their descriptions.
        options_and_functions (dict): A dictionary mapping options to their corresponding functions.
        scanner: An object used for scanning user input.
        printer: An object used for printing menu options and messages.

    Methods:
        option_present(option): Checks if an option is present in the menu.
        invoke_function(option): Invokes the function corresponding to the given menu option.
        print_menu(): Prints the menu options.
        scan_and_invoke_option(): Scans user input for a menu option and invokes the corresponding function.
    """

    def __init__(self, configuration):
        """
        Initializes the Menu with the given configuration.

        Args:
            configuration: An object containing configuration settings for the menu.
        """
        self.configuration = configuration
        self.options_and_descriptions = configuration.menu_configuration.options_and_descriptions
        self.options_and_functions = configuration.menu_configuration.options_and_functions
        self.scanner = configuration.menu_configuration.scanner
        self.printer = configuration.menu_configuration.printer

    def __handle_not_present_option(self):
        """
        Handles the situation when an invalid menu option is selected.

        Raises:
            InvalidOption: If the selected option is not present in the menu.
        """
        raise InvalidOption('Invalid option specified')

    def option_present(self, option):
        """
        Checks if the given option is present in the menu.

        Args:
            option (str): The menu option to check.

        Returns:
            bool: True if the option is present in the menu, False otherwise.
        """
        return option in self.options_and_functions

    def invoke_function(self, option):
        """
        Invokes the function corresponding to the given menu option.

        Args:
            option (str): The menu option selected by the user.

        Raises:
            InvalidOption: If the selected option is not present in the menu.
        """
        if not self.option_present(option):
            self.__handle_not_present_option()
        self.options_and_functions[option]()

    def print_menu(self):
        """
        Prints the menu options to the console.
        """
        self.printer.clear_console()
        for option in list(self.options_and_descriptions.keys()):
            if option == '0':
                self.printer.print('')
            self.printer.print('[' + option + '] - ' + self.options_and_descriptions[option])
        self.printer.print('')

    def scan_and_invoke_option(self):
        """
        Scans user input for a menu option and invokes the corresponding function.
        """
        option = self.scanner.scan()
        self.printer.clear_console()
        self.invoke_function(option)

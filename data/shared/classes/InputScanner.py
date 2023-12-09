from data.shared.exception.EmptyInput import EmptyInput

class InputScanner:
    """
    A class for handling user input in the application.

    This class provides methods to scan user input from the console, with options to handle empty inputs
    and await user action to continue the application flow.

    Attributes:
        printer: An object used for printing messages or alerts.

    Methods:
        scan(prompt='', allow_empty=False): Scans user input from the console with an optional prompt.
        input_empty(input_string): Static method to check if the input string is empty or contains only whitespace.
        await_user_input(): Static method to pause the application and wait for the user to press Enter.
    """

    def __init__(self, printer):
        """
        Initializes the InputScanner with a printer object.

        Args:
            printer: An object used for printing messages or alerts.
        """
        self.printer = printer

    def __handle_empty_input(self):
        """
        Handles the situation when an empty input is provided by the user.

        Raises:
            EmptyInput: If the input provided is empty.
        """
        raise EmptyInput('Input cannot be empty')

    def scan(self, prompt='', allow_empty=False):
        """
        Scans user input from the console. Optionally, a prompt message can be displayed.

        Args:
            prompt (str, optional): A message to display as a prompt for the input. Defaults to ''.
            allow_empty (bool, optional): Specifies whether empty input is allowed. Defaults to False.

        Returns:
            str: The user input as a string.

        Raises:
            EmptyInput: If empty input is not allowed and the user provides an empty input.
        """
        input_string = input(prompt)

        if not allow_empty and InputScanner.input_empty(input_string):
            self.__handle_empty_input()

        return input_string
        
    @staticmethod
    def input_empty(input_string):
        """
        Checks if the provided input string is empty or consists only of whitespace.

        Args:
            input_string (str): The input string to check.

        Returns:
            bool: True if the input string is empty or contains only whitespace, False otherwise.
        """
        return input_string == "" or input_string.isspace()
    
    @staticmethod
    def await_user_input():
        """
        Pauses the application and waits for the user to press Enter.
        """
        input('Press Enter to continue...')
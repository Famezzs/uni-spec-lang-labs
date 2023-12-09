# Class which is used for exception handling
class ExceptionHandler:
    """
    A class for handling exceptions within the application.

    This class provides functionality to display exception messages, log them, and pause the application flow until
    the user acknowledges the exception.

    Attributes:
        configuration: Configuration object containing settings for exception handling.
        printer: Object used for printing messages to the console.
        scanner: Object used for scanning user inputs.

    Methods:
        handle(exception): Handle the exception that occured in the application.
    """
    
    def __init__(self, configuration):
        self.configuration = configuration
        self.printer = configuration.exception_handler_configuration.printer
        self.scanner = configuration.exception_handler_configuration.scanner
    
    def handle(self, exception: Exception):
        self.printer.clear_console()
        self.printer.print(exception, True)
        self.configuration.logger.log_warning(f"{exception}-{exception.__traceback__}")
        self.scanner.await_user_input()
        self.printer.clear_console()
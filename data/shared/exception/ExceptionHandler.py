# Class which is used for exception handling
class ExceptionHandler:
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
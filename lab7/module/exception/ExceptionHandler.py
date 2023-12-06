# Class which used used for exception handling
class ExceptionHandler:
    def __init__(self, configuration):
        self.printer = configuration.exception_handler_configuration.printer
        self.scanner = configuration.exception_handler_configuration.scanner
    
    def handle(self, exception):
        self.printer.clear_console()
        self.printer.print(exception, True)
        self.scanner.await_user_input()
        self.printer.clear_console()
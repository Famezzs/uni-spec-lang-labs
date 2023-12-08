from data.shared.classes.Menu import Menu
from data.shared.exception.ExceptionHandler import ExceptionHandler
from data.shared.configuration.Configuration import Configuration

# Function which implements the runtime program
class Program:
    def run(self):        
        menu = Menu(Configuration)
        exceptionHandler = ExceptionHandler(Configuration)
        while True:
            try:
                menu.print_menu()
                menu.scan_and_invoke_option()
            except Exception as exception:
                exceptionHandler.handle(exception)
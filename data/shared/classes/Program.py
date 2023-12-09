from data.shared.classes.Menu import Menu
from data.shared.exception.ExceptionHandler import ExceptionHandler
from data.shared.configuration.Configuration import Configuration


class Program:
    """
    The main class that implements the runtime program.

    This class handles the program flow, including displaying the menu, processing user input,
    and handling exceptions.

    Methods:
        run(): Starts and manages the main loop of the program.
    """

    def run(self):
        """
        Starts and manages the main loop of the program.

        Continuously displays the menu, processes user selections, and handles any exceptions that occur.
        """
        menu = Menu(Configuration)
        exception_handler = ExceptionHandler(Configuration)

        while True:
            try:
                menu.print_menu()
                menu.scan_and_invoke_option()
            except Exception as exception:
                exception_handler.handle(exception)

from data.shared.classes.InputScanner import InputScanner
from data.shared.classes.OutputPrinter import OutputPrinter


class ExceptionHandlerConfiguration:
    """
    A configuration class for the ExceptionHandler class.

    This class specifies the dependencies that an ExceptionHandler class instance should use, particularly
    for output printing and input scanning.

    Attributes:
        printer: The OutputPrinter class to be used for printing messages.
        scanner: The InputScanner class to be used for scanning user inputs.
    """

    printer = OutputPrinter
    scanner = InputScanner

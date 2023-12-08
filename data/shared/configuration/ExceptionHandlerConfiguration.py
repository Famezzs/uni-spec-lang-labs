from data.shared.classes.InputScanner import InputScanner
from data.shared.classes.OutputPrinter import OutputPrinter

# Class which specifies how the ExceptionHandler class instance should behave
class ExceptionHandlerConfiguration:
    printer = OutputPrinter
    scanner = InputScanner
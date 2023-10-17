from module.abstract.Scanner import Scanner

class InputScanner(Scanner):
    @staticmethod
    def scan(prompt='', allow_empty=False):
        input_string = input(prompt)
        
        if allow_empty == False and InputScanner.input_empty(input_string) == True:
            print('Input cannot be empty')
            return InputScanner.scan(prompt)
        
        return input_string
        
    @staticmethod
    def input_empty(input_string):
        return input_string == "" or input_string.isspace() == True
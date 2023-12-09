import os
import json
import uuid


class Calculator:
    """
    A class to implement basic calculator functionality including operations like addition, 
    subtraction, multiplication, division, power, root, and modulo. It also handles logs 
    of calculations.

    Attributes:
        logs_path (str): Path to the log file where the calculation logs are stored.
        logs (list): A list of dictionaries containing calculation logs.

    Methods:
        __init__(self, logs_path='logs.json'): Initializes the calculator, setting up the logs file.
        add(self, augend, addend): Performs addition and returns the result.
        subtract(self, minuend, subtrahend): Performs subtraction and returns the result.
        multiply(self, multiplier, multiplicand): Performs multiplication and returns the result.
        divide(self, numerator, denominator): Performs division and returns the result, handles division by zero.
        power(self, base, exponent): Returns the result of raising a number to a power.
        root(self, radicand, degree): Returns the nth root of a number.
        modulo(self, dividend, divisor): Returns the remainder of division.
        get_operator(self, valid_operators={'+', '-', '*', '/'}): Prompts the user to select an operator.
        get_operand(self): Prompts the user to enter a numeric value or use a value from logs.
        get_operands(self, operator, operators_and_operand_names): Retrieves operands for a given operation.
        perform_operation(self, operator, operands): Performs the selected operation with provided operands.
        determine_continuation(self): Determines whether to continue with another calculation.
        initialize_logs_file(self, logs_path='logs.json'): Initializes the logs file.
        get_logs(self, logs_path='logs.json'): Retrieves logs from the specified path.
        append_logs(self, operands, operator, result, logs): Appends a new entry to the logs.
        save_logs_file(self): Saves the current logs to the log file.
        perform_calculation(self): Main method to perform a calculation.
        display_logs(self): Displays the calculation logs.
        load_logs(self): Loads calculation logs from a specified file path.
    """

    def __init__(self, logs_path='logs/calculator_logs.json'):
        self.logs_path = logs_path
        self.initialize_logs_file(self.logs_path)
        self.logs = self.get_logs(self.logs_path)

    def add(self, augend, addend):
        return augend + addend

    def subtract(self, minuend, subtrahend):
        return minuend - subtrahend

    def multiply(self, multiplier, multiplicand):
        return multiplier * multiplicand

    def divide(self, numerator, denominator):
        if denominator != 0:
            return numerator / denominator
        else:
            raise Exception('Division by zero is prohibited')

    def power(self, base, exponent):
        return pow(base, exponent)

    def root(self, radicand, degree):
        return radicand ** (1 / degree)

    def modulo(self, dividend, divisor):
        return dividend % divisor

    def get_operator(self, valid_operators={'+', '-', '*', '/'}):
        operator = input('Select one operator ("+", or "-", or "*", or "/", or "^", or "rt", or "%"): ')
        if operator in valid_operators:
            return operator
        else:
            print('Invalid operator. Please try again')
            return self.get_operator(valid_operators)

    def get_operand(self):
        option = ''
        operand_retrieved = False
        while operand_retrieved == False:
            option = input('\nSelect one option:\n[1] Enter a numeric value\n[2] Use the result from logs instead\n')

            match option:
                case '1':
                    try:
                        return float(input('Enter a numeric value: '))
                    except:
                        print('Entered value is not numeric', end='')
                        continue
                case '2':
                    id = input('Enter the ID of the log: ')
                    desired_log = None
                    for log in self.logs:
                        if log['id'].startswith(id):
                            desired_log = log
                            break

                    if desired_log == None:
                        print('Log with such ID was not found', end='')
                        continue
                    else:
                        print('Value retrieved:', desired_log['result'])
                        return desired_log['result']

                case '_':
                    print('Wrong option. Please try again')

    def get_operands(self, operator, operators_and_operand_names):
        print('\nInput ', operators_and_operand_names[operator][0], '(', operators_and_operand_names[operator][2], ')')
        first_operand = self.get_operand()
        print('\nInput ', operators_and_operand_names[operator][1], '(', operators_and_operand_names[operator][2], ')')
        second_operand = self.get_operand()
        return [first_operand, second_operand]

    def perform_operation(self, operator, operands):
        return self.operators_and_functions[operator](self, operands[0], operands[1])

    def determine_continuation(self):
        decision = input('Continue? Y/N: ')
        if decision.lower() == 'y' or decision.lower() == 'yes':
            return True
        return False

    def initialize_logs_file(self, logs_path='logs.json'):
        if os.path.isfile(logs_path) == False:
            logs_file = open(logs_path, 'w')
            logs_file.write('[]')
            logs_file.close()

    def get_logs(self, logs_path='logs.json'):
        logs_file = open(logs_path)
        logs_string = logs_file.read()
        logs_file.close()
        if len(logs_string) != 0:
            return json.loads(logs_string)
        else:
            return []

    def append_logs(self, operands, operator, result, logs):
        logs.append({"id": str(uuid.uuid4()), "operands": operands, "operator": operator, "result": result})

    def save_logs_file(self):
        logs_file = open(self.logs_path, 'w')
        logs_file.write(json.dumps(self.logs))
        logs_file.close()

    operators_and_functions = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '^': power,
        'rt': root,
        '%': modulo
    }

    operators_and_operand_names = {
        '+': ['augend', 'addend', 'augend + addend'],
        '-': ['minuend', 'subtrahend', 'minuend - subtrahend'],
        '*': ['multiplier', 'multiplicand', 'multiplier * multiplicand'],
        '/': ['numerator', 'denominator', 'numerator / denominator'],
        '^': ['base', 'exponent', 'base ^ exponent'],
        'rt': ['radicand', 'degree', 'radicand ^ (1 / degree)'],
        '%': ['dividend', 'divisor', 'dividend mod divisor']
    }

    def perform_calculation(self):
        continue_calculation = True
        while continue_calculation == True:
            operator = self.get_operator(list(self.operators_and_functions.keys()))
            operands = self.get_operands(operator, self.operators_and_operand_names)
            result = self.perform_operation(operator, operands)
            print('Result: ', result)
            self.append_logs(operands, operator, result, self.logs)
            continue_calculation = self.determine_continuation()

    def display_logs(self):
        print('\n\nLogs:')
        for log in self.logs:
            print('id:', log['id'])
            print('expression:', log['operands'][0], log['operator'], log['operands'][1], '=', log['result'],
                  end='\n\n')

    def load_logs(self):
        path = input('Specify path to logs file: ')
        if os.path.isdir(path) == True:
            print('Specified file is a directory. Try again')
            self.load_logs()

        if os.path.isfile(path) == True:
            self.logs = self.get_logs(path)
            self.logs_path = path
            print('Successfully retrieved the logs')
        else:
            print('Specified file does not exist')

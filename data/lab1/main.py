import os
import json
import uuid

logs_path = 'logs.json'
logs = []


def add(augend, addend):
    return augend + addend


def subtract(minuend, subtrahend):
    return minuend - subtrahend


def multiply(multiplier, multiplicand):
    return multiplier * multiplicand


def divide(numerator, denominator):
    if denominator != 0:
        return numerator / denominator
    else:
        print('Division by zero is prohibited')


def power(base, exponent):
    return pow(base, exponent)


def root(radicand, degree):
    return radicand ** (1 / degree)


def modulo(dividend, divisor):
    return dividend % divisor


def get_operator(valid_operators={'+', '-', '*', '/'}):
    operator = input('Select one operator ("+", or "-", or "*", or "/", or "^", or "rt", or "%"): ')
    if operator in valid_operators:
        return operator
    else:
        print('Invalid operator. Please try again')
        return get_operator(valid_operators)


def get_operand():
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
                for log in logs:
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


def get_operands(operator, operators_and_operand_names):
    print('\nInput ', operators_and_operand_names[operator][0], '(', operators_and_operand_names[operator][2], ')')
    first_operand = get_operand()
    print('\nInput ', operators_and_operand_names[operator][1], '(', operators_and_operand_names[operator][2], ')')
    second_operand = get_operand()
    return [first_operand, second_operand]


def perform_operation(operators_and_functions, operator, operands):
    return operators_and_functions[operator](operands[0], operands[1])


def determine_continuation():
    decision = input('Continue? Y/N: ')
    if decision.lower() == 'y' or decision.lower() == 'yes':
        return True
    return False


def initialize_logs_file(logs_path='logs.json'):
    if os.path.isfile(logs_path) == False:
        logs_file = open(logs_path, 'w')
        logs_file.write('[]')
        logs_file.close()


def get_logs(logs_path='logs.json'):
    logs_file = open(logs_path)
    logs_string = logs_file.read()
    logs_file.close()
    if len(logs_string) != 0:
        return json.loads(logs_string)
    else:
        return []


def append_logs(operands, operator, result, logs):
    logs.append({"id": str(uuid.uuid4()), "operands": operands, "operator": operator, "result": result})


def save_logs_file(logs_path, logs):
    logs_file = open(logs_path, 'w')
    logs_file.write(json.dumps(logs))
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


def perform_calculation():
    continue_calculation = True
    while continue_calculation == True:
        operator = get_operator(list(operators_and_functions.keys()))
        operands = get_operands(operator, operators_and_operand_names)
        result = perform_operation(operators_and_functions, operator, operands)
        print('Result: ', result)
        append_logs(operands, operator, result, logs)
        continue_calculation = determine_continuation()


def display_logs():
    print('\n\nLogs:')
    for log in logs:
        print('id:', log['id'])
        print('expression:', log['operands'][0], log['operator'], log['operands'][1], '=', log['result'], end='\n\n')


def load_logs():
    path = input('Specify path to logs file: ')
    if os.path.isdir(path) == True:
        print('Specified file is a directory. Try again')
        load_logs()

    if os.path.isfile(path) == True:
        global logs
        logs = get_logs(path)
        global logs_path
        logs_path = path
        print('Successfully retrieved the logs')
    else:
        print('Specified file does not exist')


def exit_program():
    save_logs_file(logs_path, logs)


options_and_functions = {
    '1': perform_calculation,
    '2': display_logs,
    '3': load_logs,
    '0': exit_program
}


def main():
    option = ''
    initialize_logs_file(logs_path)
    global logs
    logs = get_logs(logs_path)

    while option != '0':
        option = input(
            '\nSelect one option:\n[1] - Perform calculation\n[2] - Display logs\n[3] - Load logs\n\n[0] - Exit\n')
        options_and_functions[option]()


main()

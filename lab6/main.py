from module.Calculator import Calculator


def main():
    option = ''
    calculator = Calculator()

    while option != '0':
        option = input('\nSelect one option:\n[1] - Perform calculation\n[2] - Display logs\n[3] - Load logs\n\n[0] - Exit\n')
        match option:
            case '1':
                calculator.perform_calculation()
            case '2':
                calculator.display_logs()
            case '3':
                calculator.load_logs()
            case '0':
                calculator.save_logs_file() 

main()
from data.lab6.module.Calculator import Calculator

# Class which stores the functions called by the Menu class instance
class MenuFunctions:
    __calculator = Calculator()

    @staticmethod 
    def __read_csv_file():
        from data.shared.configuration.Configuration import Configuration
        from data.lab8.module.helpers.CSVFileReader import CSVFileReader
        reader = CSVFileReader(Configuration)
        return reader.read()

    @staticmethod
    def __get_plot_values(allow_save_to_file = False):
        from data.shared.classes.InputScanner import InputScanner
        from data.shared.classes.OutputPrinter import OutputPrinter
        from data.shared.configuration.Configuration import Configuration
        scanner = InputScanner(OutputPrinter)
        
        plot_title = scanner.scan('Plot Title: ', True)
        if InputScanner.input_empty(plot_title):
            plot_title = Configuration.analysis_configuration.default_plot_title
        
        x_plot_label = scanner.scan('X Plot Label: ', True)
        if InputScanner.input_empty(x_plot_label):
            x_plot_label = Configuration.analysis_configuration.default_x_plot_label

        x_plot_property = scanner.scan('X Plot Property: ', True)
        if InputScanner.input_empty(x_plot_property):
            x_plot_property = Configuration.analysis_configuration.default_x_plot_property

        y_plot_label = scanner.scan('Y Plot Label: ', True)
        if InputScanner.input_empty(y_plot_label):
            y_plot_label = Configuration.analysis_configuration.default_y_plot_label
        
        y_plot_property = scanner.scan('Y Plot Property: ', True)
        if InputScanner.input_empty(y_plot_property):
            y_plot_property = Configuration.analysis_configuration.default_y_plot_property

        export_full_file_name = ''

        if allow_save_to_file == True:
            option = scanner.scan('Export result? (Y/N): ', True)
            if option.lower().startswith('y'):
                export_full_file_name = scanner.scan('Full file name: ')

        return {
            'plot_title': plot_title,
            'x_plot_label': x_plot_label,
            'x_plot_property': x_plot_property,
            'y_plot_label': y_plot_label,
            'y_plot_property': y_plot_property,
            'export_full_file_name': export_full_file_name
        }

    @staticmethod
    def __get_histogram_values(allow_save_to_file = False):
        from data.shared.classes.InputScanner import InputScanner
        from data.shared.classes.OutputPrinter import OutputPrinter
        from data.shared.configuration.Configuration import Configuration
        scanner = InputScanner(OutputPrinter)

        histogram_title = scanner.scan('Histogram Title: ', True)
        if InputScanner.input_empty(histogram_title):
            histogram_title = Configuration.analysis_configuration.default_histogram_title
        
        x_histogram_label = scanner.scan('X Histogram Label: ', True)
        if InputScanner.input_empty(x_histogram_label):
            x_histogram_label = Configuration.analysis_configuration.default_x_histogram_label

        y_histogram_label = scanner.scan('Y Histogram Label: ', True)
        if InputScanner.input_empty(y_histogram_label):
            y_histogram_label = Configuration.analysis_configuration.default_y_histogram_label
        
        histogram_property = scanner.scan('Histogram Property: ', True)
        if InputScanner.input_empty(histogram_property):
            histogram_property = Configuration.analysis_configuration.default_histogram_property

        export_full_file_name = ''

        if allow_save_to_file == True:
            option = scanner.scan('Export result? (Y/N): ', True)
            if option.lower().startswith('y'):
                export_full_file_name = scanner.scan('Full file name: ')
            
        return {
            'histogram_title': histogram_title,
            'x_histogram_label': x_histogram_label,
            'y_histogram_label': y_histogram_label,
            'histogram_property': histogram_property,
            'export_full_file_name': export_full_file_name
        }
    
    @staticmethod
    def text_to_art_library():
        from data.lab3.module.ArtGenerator import ArtGenerator
        from data.shared.classes.InputScanner import InputScanner
        from data.shared.classes.OutputPrinter import OutputPrinter
        scanner = InputScanner(OutputPrinter)

        text = scanner.scan('Text to transform: ')
        font = scanner.scan('Font (leave blank for default): ', allow_empty=True)
        color = scanner.scan('Color (leave blank for default): ', allow_empty=True)

        if InputScanner.input_empty(font) == True:
            font = ArtGenerator.default_font    

        result = ArtGenerator.text_to_art(text=text, font=font)
        MenuFunctions.print_art(result, color)
        
        option = scanner.scan('Scale art? (Y/N): ')
        if option.startswith('y'):
            result = MenuFunctions.scale_art(result)
            MenuFunctions.print_art(result, color)

        option = scanner.scan('Save to file? (Y/N): ')
        if option.startswith('y'):
            MenuFunctions.save_to_file(result)

    @staticmethod
    def display_fonts():
        from data.lab3.module.ArtGenerator import ArtGenerator
        from data.shared.classes.ArtPrinter import ArtPrinter
        from data.shared.classes.InputScanner import InputScanner
        print('Available fonts:')
        ArtPrinter.print(ArtGenerator.get_fonts())
        InputScanner.await_user_input()


    @staticmethod
    def print_art(result, color):
        from data.shared.classes.ArtPrinter import ArtPrinter
        from data.shared.classes.InputScanner import InputScanner
        if InputScanner.input_empty(color) == True:
            ArtPrinter.print(result)
        else:
            ArtPrinter.colored_print(result, color)

    @staticmethod
    def save_to_file(content):
        from data.shared.classes.InputScanner import InputScanner
        from data.shared.classes.OutputPrinter import OutputPrinter
        scanner = InputScanner(OutputPrinter)

        path = scanner.scan('Specify path to the file: ')
        file = open(path, 'a')
        file.write(content)
        file.close()

    @staticmethod
    def scale_art(content):
        from data.shared.classes.ArtScaler import ArtScaler
        from data.shared.classes.InputScanner import InputScanner
        from data.shared.classes.OutputPrinter import OutputPrinter
        scanner = InputScanner(OutputPrinter)

        multiplier = scanner.scan('Specify integer multiplier: ')
        return ArtScaler.scale(int(multiplier), content)    

    @staticmethod
    def text_to_art_own():
        from data.lab4.module.ArtGenerator import ArtGenerator
        from data.shared.classes.InputScanner import InputScanner
        from data.shared.classes.OutputPrinter import OutputPrinter
        from data.shared.configuration.Configuration import Configuration
        scanner = InputScanner(OutputPrinter)

        text = scanner.scan('Text to transform: ')
        character = scanner.scan('Base character (leave blank for default): ', allow_empty=True)
        color = scanner.scan('Color (leave blank for default): ', allow_empty=True)

        art_generator = ArtGenerator(Configuration)

        result = art_generator.text_to_art(text, character)
        MenuFunctions.print_art(result, color)
        
        option = scanner.scan('Scale art? (Y/N): ')
        if option.lower().startswith('y'):
            result = MenuFunctions.scale_art(result)
            MenuFunctions.print_art(result, color)

        option = scanner.scan('Save to file? (Y/N): ')
        if option.lower().startswith('y'):
            MenuFunctions.save_to_file(result)

    @staticmethod
    def draw_figure():
        from data.shared.classes.InputScanner import InputScanner
        from data.shared.classes.OutputPrinter import OutputPrinter
        from data.lab5.module.FigureGenerator import FigureGenerator
        scanner = InputScanner(OutputPrinter)

        width = float(scanner.scan('Width: '))
        length = float(scanner.scan('Length: '))
        height = float(scanner.scan('Height: '))
        color = scanner.scan('Color: ')
        x_axes_angle_coefficient = scanner.scan('X Axes Angle Coefficient (defaults to 0.5): ', allow_empty=True)
        y_axes_angle_coefficient = scanner.scan('Y Axes Angle Coefficient (defaults to 0.5): ', allow_empty=True)

        if InputScanner.input_empty(x_axes_angle_coefficient):
            x_axes_angle_coefficient = FigureGenerator.x_axes_default_coefficient
        else:
            x_axes_angle_coefficient = float(x_axes_angle_coefficient)

        if InputScanner.input_empty(y_axes_angle_coefficient):
            y_axes_angle_coefficient = FigureGenerator.y_axes_default_coefficient
        else:
            y_axes_angle_coefficient = float(y_axes_angle_coefficient)

        figure_generator = FigureGenerator(x_axes_angle_coefficient, y_axes_angle_coefficient)

        figure_generator.draw_parallelepiped(width, length, height, color)

    @staticmethod
    def perform_calculation():
        MenuFunctions.__calculator.perform_calculation()

    @staticmethod
    def display_calculator_logs():
        from data.shared.classes.InputScanner import InputScanner
        MenuFunctions.__calculator.display_logs()
        InputScanner.await_user_input()
    
    @staticmethod
    def load_calculator_logs():
        MenuFunctions.__calculator.load_logs()

    @staticmethod
    def generate_csv_file():
        from data.shared.configuration.Configuration import Configuration
        from data.lab8.module.helpers.CSVFileGenerator import CSVFileGenerator
        generator = CSVFileGenerator(Configuration)
        generator.generate()
    
    @staticmethod
    def plot():
        from data.lab8.module.DataAnalyser import DataAnalyser
        analyser = DataAnalyser(MenuFunctions.__read_csv_file())
        analyser.plot(MenuFunctions.__get_plot_values(True))

    @staticmethod
    def histogram():
        from data.lab8.module.DataAnalyser import DataAnalyser
        analyser = DataAnalyser(MenuFunctions.__read_csv_file())
        analyser.histogram(MenuFunctions.__get_histogram_values(True))      

    @staticmethod
    def plot_and_histogram():
        from data.lab8.module.DataAnalyser import DataAnalyser
        analyser = DataAnalyser(MenuFunctions.__read_csv_file())
        analyser.plot_and_histogram(MenuFunctions.__get_plot_values(False), MenuFunctions.__get_histogram_values(False))
        
    @staticmethod
    def __get_color_input():
        from data.shared.classes.InputScanner import InputScanner
        from data.shared.classes.OutputPrinter import OutputPrinter
        scanner = InputScanner(OutputPrinter)
        return scanner.scan('Color: ')
    
    @staticmethod
    def __save_output_as_file(data):
        from data.lab7.module.helpers.SaveAsFile import SaveAsFile
        from data.shared.classes.InputScanner import InputScanner
        from data.shared.classes.OutputPrinter import OutputPrinter
        scanner = InputScanner(OutputPrinter)
        option = scanner.scan('Save to file? (Y/N): ', True) 
        if not option.startswith('y'):
            return
        from tabulate import tabulate
        content = tabulate(data, headers="keys")
        full_file_name = scanner.scan('Full file name: ')
        SaveAsFile.save_as_file(content, full_file_name)

    @staticmethod
    def print_all_users():
        from data.lab7.module.APICaller import APICaller
        from data.lab7.module.helpers.UserDataFilter import UserDataFilter
        from data.shared.classes.OutputPrinter import OutputPrinter
        from data.shared.configuration.Configuration import Configuration
        api_caller = APICaller(Configuration)
        users = api_caller.get_all_users()
        filtered_users = UserDataFilter.filter(users)
        OutputPrinter.print_as_colored_table(filtered_users, MenuFunctions.__get_color_input(), True)
        MenuFunctions.__save_output_as_file(filtered_users)

    @staticmethod
    def print_all_posts():
        from data.lab7.module.APICaller import APICaller
        from data.lab7.module.helpers.PostDataFilter import PostDataFilter
        from data.shared.classes.OutputPrinter import OutputPrinter
        from data.shared.configuration.Configuration import Configuration
        api_caller = APICaller(Configuration)
        posts = api_caller.get_all_posts()
        filtered_posts = PostDataFilter.filter(posts)
        OutputPrinter.print_as_colored_table(filtered_posts, MenuFunctions.__get_color_input(), True)
        MenuFunctions.__save_output_as_file(filtered_posts)

    @staticmethod
    def print_all_comments():
        from data.lab7.module.APICaller import APICaller
        from data.lab7.module.helpers.CommentDataFilter import CommentDataFilter
        from data.shared.classes.OutputPrinter import OutputPrinter
        from data.shared.configuration.Configuration import Configuration
        api_caller = APICaller(Configuration)
        comments = api_caller.get_all_comments()
        filtered_comments = CommentDataFilter.filter(comments)
        OutputPrinter.print_as_colored_table(filtered_comments, MenuFunctions.__get_color_input(), True)
        MenuFunctions.__save_output_as_file(filtered_comments)
    
    @staticmethod
    def exit_program():
        MenuFunctions.__calculator.save_logs_file()
        exit(0)
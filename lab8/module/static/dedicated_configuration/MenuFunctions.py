# Class which stores the functions called by the Menu class instance
class MenuFunctions:
    @staticmethod 
    def __read_csv_file():
        from module.static.Configuration import Configuration
        from module.helpers.CSVFileReader import CSVFileReader
        reader = CSVFileReader(Configuration)
        return reader.read()

    @staticmethod
    def __get_plot_values(allow_save_to_file = False):
        from module.InputScanner import InputScanner
        from module.OutputPrinter import OutputPrinter
        from module.static.Configuration import Configuration
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
        from module.InputScanner import InputScanner
        from module.OutputPrinter import OutputPrinter
        from module.static.Configuration import Configuration
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
    def generate_csv_file():
        from module.static.Configuration import Configuration
        from module.helpers.CSVFileGenerator import CSVFileGenerator
        generator = CSVFileGenerator(Configuration)
        generator.generate()
    
    @staticmethod
    def plot():
        from module.DataAnalyser import DataAnalyser
        analyser = DataAnalyser(MenuFunctions.__read_csv_file())
        analyser.plot(MenuFunctions.__get_plot_values(True))

    @staticmethod
    def histogram():
        from module.DataAnalyser import DataAnalyser
        analyser = DataAnalyser(MenuFunctions.__read_csv_file())
        analyser.histogram(MenuFunctions.__get_histogram_values(True))      

    @staticmethod
    def plot_and_histogram():
        from module.DataAnalyser import DataAnalyser
        analyser = DataAnalyser(MenuFunctions.__read_csv_file())
        analyser.plot_and_histogram(MenuFunctions.__get_plot_values(False), MenuFunctions.__get_histogram_values(False))
        
    @staticmethod
    def exit_program():
        exit(0)
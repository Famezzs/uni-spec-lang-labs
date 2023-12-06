class DataAnalyser:
    def __init__(self, dataset):
        self.dataset = dataset

    def __export_plot(self, plot_parameters):
        import matplotlib.pyplot as pyplot
        pyplot.plot(self.dataset[plot_parameters['x_plot_property']], self.dataset[plot_parameters['y_plot_property']])
        pyplot.title(plot_parameters['plot_title'])
        pyplot.xlabel(plot_parameters['x_plot_label'])
        pyplot.ylabel(plot_parameters['y_plot_label'])
        pyplot.savefig(plot_parameters['export_full_file_name'])
        pyplot.close()

    def __export_histogram(self, histogram_parameters):
        import matplotlib.pyplot as pyplot
        pyplot.hist(self.dataset[histogram_parameters['histogram_property']], bins=15)
        pyplot.title(histogram_parameters['histogram_title'])
        pyplot.xlabel(histogram_parameters['x_histogram_label'])
        pyplot.ylabel(histogram_parameters['y_histogram_label'])
        pyplot.savefig(histogram_parameters['export_full_file_name'])
        pyplot.close()

    def find_min_max(self):
        return [self.dataset.min(), self.dataset.max()]
    
    def plot(self, plot_parameters):
        import matplotlib.pyplot as pyplot
        from module.InputScanner import InputScanner
        pyplot.plot(self.dataset[plot_parameters['x_plot_property']], self.dataset[plot_parameters['y_plot_property']])
        pyplot.title(plot_parameters['plot_title'])
        pyplot.xlabel(plot_parameters['x_plot_label'])
        pyplot.ylabel(plot_parameters['y_plot_label'])
        pyplot.show()
        pyplot.close()

        if not InputScanner.input_empty(plot_parameters['export_full_file_name']):
            self.__export_plot(plot_parameters)

    def histogram(self, histogram_parameters):
        import matplotlib.pyplot as pyplot
        from module.InputScanner import InputScanner
        pyplot.hist(self.dataset[histogram_parameters['histogram_property']], bins=15)
        pyplot.title(histogram_parameters['histogram_title'])
        pyplot.xlabel(histogram_parameters['x_histogram_label'])
        pyplot.ylabel(histogram_parameters['y_histogram_label'])
        pyplot.show()
        pyplot.close()

        if not InputScanner.input_empty(histogram_parameters['export_full_file_name']):
            self.__export_histogram(histogram_parameters)
    
    def plot_and_histogram(self, plot_parameters, histogram_parameters):
        import matplotlib.pyplot as pyplot
        figure, axis = pyplot.subplots(2, 1, figsize=(10, 8))
        axis[0].plot(self.dataset[plot_parameters['x_plot_property']], self.dataset[plot_parameters['y_plot_property']])
        axis[0].set_title(plot_parameters['plot_title'])
        axis[0].set_xlabel(plot_parameters['x_plot_label'])
        axis[0].set_ylabel(plot_parameters['y_plot_label'])
        axis[1].hist(self.dataset[histogram_parameters['histogram_property']], bins=15)
        axis[1].set_title(histogram_parameters['histogram_title'])
        axis[1].set_xlabel(histogram_parameters['x_histogram_label'])
        axis[1].set_ylabel(histogram_parameters['y_histogram_label'])
        pyplot.tight_layout()
        pyplot.show()
        pyplot.close()
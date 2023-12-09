class DataAnalyser:
    """
    A class for analyzing and visualizing data using plots and histograms.

    This class provides methods for finding the minimum and maximum values in a dataset, 
    plotting data, creating histograms, and exporting these visualizations as images.

    Attributes:
        dataset (DataFrame): A pandas DataFrame containing the dataset to be analyzed.

    Methods:
        find_min_max(): Finds the minimum and maximum values in the dataset.
        plot(plot_parameters): Plots data based on provided parameters and optionally exports the plot as an image.
        histogram(histogram_parameters): Creates a histogram based on provided parameters and optionally exports it as an image.
        plot_and_histogram(plot_parameters, histogram_parameters): Simultaneously creates a plot and histogram based on provided parameters and displays them.
    """

    def __init__(self, dataset):
        """
        Initializes the DataAnalyser with a dataset.

        Args:
            dataset (DataFrame): A pandas DataFrame containing the dataset to be analyzed.
        """
        self.dataset = dataset

    def __export_plot(self, plot_parameters):
        """
        Generates and exports a plot based on the provided plot parameters.

        Args:
            plot_parameters (dict): A dictionary containing parameters for the plot.
        """
        import matplotlib.pyplot as pyplot
        pyplot.plot(self.dataset[plot_parameters['x_plot_property']], self.dataset[plot_parameters['y_plot_property']])
        pyplot.title(plot_parameters['plot_title'])
        pyplot.xlabel(plot_parameters['x_plot_label'])
        pyplot.ylabel(plot_parameters['y_plot_label'])
        pyplot.savefig(plot_parameters['export_full_file_name'])
        pyplot.close()

    def __export_histogram(self, histogram_parameters):
        """
        Generates and exports a histogram based on the provided histogram parameters.

        Args:
            histogram_parameters (dict): A dictionary containing parameters for the histogram.
        """
        import matplotlib.pyplot as pyplot
        pyplot.hist(self.dataset[histogram_parameters['histogram_property']], bins=15)
        pyplot.title(histogram_parameters['histogram_title'])
        pyplot.xlabel(histogram_parameters['x_histogram_label'])
        pyplot.ylabel(histogram_parameters['y_histogram_label'])
        pyplot.savefig(histogram_parameters['export_full_file_name'])
        pyplot.close()

    def find_min_max(self):
        """
        Finds the minimum and maximum values for each column in the dataset.

        Returns:
            tuple: A tuple containing two pandas Series, one for the minimum and one for the maximum values.
        """
        return [self.dataset.min(), self.dataset.max()]
    
    def plot(self, plot_parameters):
        """
        Generates a plot based on provided parameters and displays it. If an export file name is provided, 
        the plot is also saved as an image.

        Args:
            plot_parameters (dict): A dictionary containing parameters for the plot.
        """
        import matplotlib.pyplot as pyplot
        from data.shared.classes.InputScanner import InputScanner
        pyplot.plot(self.dataset[plot_parameters['x_plot_property']], self.dataset[plot_parameters['y_plot_property']])
        pyplot.title(plot_parameters['plot_title'])
        pyplot.xlabel(plot_parameters['x_plot_label'])
        pyplot.ylabel(plot_parameters['y_plot_label'])
        pyplot.show()
        pyplot.close()

        if not InputScanner.input_empty(plot_parameters['export_full_file_name']):
            self.__export_plot(plot_parameters)

    def histogram(self, histogram_parameters):
        """
        Generates a histogram based on provided parameters and displays it. If an export file name is provided, 
        the histogram is also saved as an image.

        Args:
            histogram_parameters (dict): A dictionary containing parameters for the histogram.
        """
        import matplotlib.pyplot as pyplot
        from data.shared.classes.InputScanner import InputScanner
        pyplot.hist(self.dataset[histogram_parameters['histogram_property']], bins=15)
        pyplot.title(histogram_parameters['histogram_title'])
        pyplot.xlabel(histogram_parameters['x_histogram_label'])
        pyplot.ylabel(histogram_parameters['y_histogram_label'])
        pyplot.show()
        pyplot.close()

        if not InputScanner.input_empty(histogram_parameters['export_full_file_name']):
            self.__export_histogram(histogram_parameters)
    
    def plot_and_histogram(self, plot_parameters, histogram_parameters):
        """
        Simultaneously generates a plot and a histogram based on provided parameters and displays them.

        Args:
            plot_parameters (dict): A dictionary containing parameters for the plot.
            histogram_parameters (dict): A dictionary containing parameters for the histogram.
        """
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

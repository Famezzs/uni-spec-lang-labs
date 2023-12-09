class AnalysisConfiguration:
    """
    A configuration class for storing settings related to data analysis and plotting.

    This class contains class-level attributes that store various configuration settings 
    used for analyzing and visualizing data, particularly sales data in a CSV format.

    Attributes:
        csv_file_name (str): The name of the CSV file containing sales data.
        default_plot_title (str): The default title for plots.
        default_x_plot_label (str): The default label for the x-axis in plots.
        default_x_plot_property (str): The default property to be plotted on the x-axis.
        default_y_plot_label (str): The default label for the y-axis in plots.
        default_y_plot_property (str): The default property to be plotted on the y-axis.
        default_histogram_title (str): The default title for histograms.
        default_x_histogram_label (str): The default label for the x-axis in histograms.
        default_y_histogram_label (str): The default label for the y-axis in histograms.
        default_histogram_property (str): The default property to be used for histograms.
    """

    csv_file_name = 'sales_data.csv'
    default_plot_title = 'Sales by Product ID'
    default_x_plot_label = 'Product ID'
    default_x_plot_property = 'Product_ID'
    default_y_plot_label = 'Sales'
    default_y_plot_property = 'Sales'
    default_histogram_title = 'Distribution of Customer Ratings'
    default_x_histogram_label = 'Rating'
    default_y_histogram_label = 'Frequency'
    default_histogram_property = 'Customer_Rating'

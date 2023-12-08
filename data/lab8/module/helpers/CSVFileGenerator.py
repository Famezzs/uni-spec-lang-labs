class CSVFileGenerator:
    def __init__(self, configuration):
        self.configuration = configuration

    def generate(self):
        import pandas
        import numpy
        import time
        numpy.random.seed(int(time.time()))
        data = {
            "Product_ID": range(1, 101),
            "Sales": numpy.random.randint(100, 1000, 100),  # Sales figures between 100 and 1000
            "Profit": numpy.random.randint(-50, 200, 100),  # Profit figures between -50 and 200
            "Customer_Rating": numpy.random.uniform(1.0, 5.0, 100)  # Customer ratings between 1.0 and 5.0
        }
        dataset = pandas.DataFrame(data)
        dataset.to_csv(self.configuration.analysis_configuration.csv_file_name, index=False)
class CSVFileReader:
    def __init__(self, configuration):
        self.configuration = configuration

    def read(self):
        import pandas
        return pandas.read_csv(self.configuration.analysis_configuration.csv_file_name)

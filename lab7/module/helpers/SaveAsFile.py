class SaveAsFile:
    @staticmethod
    def save_as_file(input_string, file_name, file_format: str):
        lower_file_format = file_format.lower()
        full_file_name = f"{file_name}.{lower_file_format}"
        with open(full_file_name, 'w') as file:
            file.write(input_string)
class SaveAsFile:
    @staticmethod
    def save_as_file(input_string, full_file_name: str):
        with open(full_file_name.lower(), 'w') as file:
            file.write(input_string)
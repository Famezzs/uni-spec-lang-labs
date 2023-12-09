class SaveAsFile:
    """
    A static utility class for saving a string to a file.

    This class provides a static method to save a given string to a file with a specified file name. 
    It handles the opening and writing of the file.

    Methods:
        save_as_file(input_string, full_file_name: str): Saves the provided string to a file with the given file name.
    """
    @staticmethod
    def save_as_file(input_string, full_file_name: str):
        """
        Saves a given string to a file with the specified file name. 

        The file name is converted to lower case before saving. The method creates a new file or overwrites 
        the existing file with the given name.

        Args:
            input_string (str): The string to be saved to the file.
            full_file_name (str): The full path and name of the file where the string will be saved.

        Note:
            The file name is converted to lower case before saving.
        """
        with open(full_file_name.lower(), 'w') as file:
            file.write(input_string)
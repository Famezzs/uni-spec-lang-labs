from data.shared.classes.InputScanner import InputScanner

class ArtGenerator:
    """
    A class for generating ASCII art from text based on a given configuration.

    The class uses a configuration object to set up various properties related to art generation 
    and provides a method to convert text to ASCII art.

    Attributes:
        letters_and_art (dict): A dictionary mapping characters to their ASCII art representation.
        elements_in_letter_array (int): Number of elements (lines) in each ASCII art representation.
        default_symbol (str): The default symbol used in ASCII art representations.

    Methods:
        text_to_art(self, text, character=''): Converts given text into ASCII art. Optionally replaces 
            the default symbol in ASCII art with a given character.
    """
    def __init__(self, configuration):
        """
        Initializes the ArtGenerator with a given configuration.

        Args:
            configuration: An object containing configuration settings for the art generator.
        """
        self.letters_and_art = configuration.art_generator_configuration.letters_and_art
        self.elements_in_letter_array = configuration.art_generator_configuration.elements_in_letter_array
        self.default_symbol = configuration.art_generator_configuration.default_symbol

    def __create_art_array(self):
        art_array = []
        for _ in range(self.elements_in_letter_array):
            art_array.append('')
        return art_array

    def __fill_in_art_array(self, art_array, text):
        for letter in text.lower():
            for i in range(self.elements_in_letter_array):
                art_array[i] += self.letters_and_art[letter][i] + ' '
        return art_array
    
    def __art_array_to_string(self, art_array):
        result = ''
        for i in range(self.elements_in_letter_array):
            result += art_array[i] + '\n'
        return result
    
    def __replace_character_in_art_string(self, art_string: str, character):
        """
        Replaces the default symbol in the ASCII art string with a given character.

        Args:
            art_string (str): The ASCII art string.
            character (str): The character to replace the default symbol with.

        Returns:
            str: The modified ASCII art string.
        """
        if InputScanner.input_empty(character) == False and character != self.default_symbol:
            art_string = art_string.replace(self.default_symbol, character)
        return art_string

    def text_to_art(self, text, character = ''):
        """
        Converts the given text into ASCII art. Optionally, a character can be specified to 
        replace the default symbol in the ASCII art.

        Args:
            text (str): The text to be converted into ASCII art.
            character (str, optional): The character to replace the default symbol in ASCII art. 
                Defaults to an empty string, which means no replacement.

        Returns:
            str: The ASCII art representation of the given text.
        """
        art_array = self.__fill_in_art_array(self.__create_art_array(), text) 
        art_string = self.__art_array_to_string(art_array)
        return self.__replace_character_in_art_string(art_string, character)
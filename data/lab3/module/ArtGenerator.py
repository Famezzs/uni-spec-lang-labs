import art


class ArtGenerator:
    """
    A class for generating ASCII art from text using the 'art' library.

    This class provides static methods to convert text to ASCII art and to retrieve 
    the list of available fonts in the 'art' library.

    Attributes:
        default_font (str): The default font used for generating ASCII art. Default is 'xcourb'.

    Methods:
        text_to_art(text, font=default_font): Converts given text into ASCII art using a specified font.
        get_fonts(): Returns a list of available fonts in the 'art' library.
    """

    default_font = 'xcourb'

    @staticmethod
    def text_to_art(text, font=default_font):
        """
        Converts the given text into ASCII art using the specified font.

        Args:
            text (str): The text to be converted into ASCII art.
            font (str, optional): The font to be used for the ASCII art. Defaults to the class's default_font.

        Returns:
            str: The ASCII art representation of the given text.
        """
        return art.text2art(text, font)

    @staticmethod
    def get_fonts():
        """
        Retrieves a list of available fonts from the 'art' library.

        Returns:
            list: A list of font names available for ASCII art generation.
        """
        return art.font_list()

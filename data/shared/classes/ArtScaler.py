from data.shared.exception.NegativeScale import NegativeScale
from data.shared.exception.FractionScale import FractionScale

class ArtScaler:
    """
    A utility class for scaling ASCII art.

    Provides static methods to scale ASCII art by a given multiplier. The scaling is performed
    both horizontally and vertically by repeating characters in each line and repeating the lines.

    Methods:
        scale(multiplier, input_string): Scales the input ASCII art by the specified multiplier.
    """

    @staticmethod
    def __validate_multiplier(multiplier):
        """
        Validates the scaling multiplier to ensure it is a non-negative integer.

        Args:
            multiplier (int): The scaling multiplier.

        Raises:
            NegativeScale: If the multiplier is negative.
            FractionScale: If the multiplier is not an integer.
        """
        if multiplier < 0:
            raise NegativeScale('Scale cannot be negative')
        if type(multiplier) != int:
            raise FractionScale('Scaler does not accept fractional multiplier')

    @staticmethod
    def scale(multiplier, input_string):
        """
        Scales the given ASCII art by the specified multiplier. The scaling is done by repeating each character 
        in a line and each line in the art, both horizontally and vertically.

        Args:
            multiplier (int): The factor by which the ASCII art is to be scaled.
            input_string (str): The ASCII art to be scaled.

        Returns:
            str: The scaled ASCII art.
        """
        ArtScaler.__validate_multiplier(multiplier)

        if multiplier == 1:
            return input_string

        result = ''
        lines = input_string.split('\n')

        for line in lines:
            scaled_line = ''.join(symbol * multiplier for symbol in line)
            result += (scaled_line + '\n') * multiplier

        return result
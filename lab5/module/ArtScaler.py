from module.abstract.Scaler import Scaler
from module.exception.NegativeScale import NegativeScale
from module.exception.FractionScale import FractionScale

class ArtScaler(Scaler):
    @staticmethod
    def scale(multiplier, input_string):
        if multiplier < 0:
            raise NegativeScale('Scale cannot be negative')
        
        if type(multiplier) != int:
            raise FractionScale('Scaler does not accept fractional multiplier')

        if multiplier == 1:
            return input_string

        result = ''

        lines = input_string.split('\n')

        for line in lines:
            scaled_line = ''
            for symbol in line:
                count = 0
                while count < multiplier:
                    scaled_line += symbol
                    count += 1
            
            count = 0
            while count < multiplier:
                result += scaled_line + '\n'
                count += 1                    

        return result
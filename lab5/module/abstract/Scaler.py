from abc import ABC, abstractmethod
    
class Scaler(ABC):
    @staticmethod
    @abstractmethod
    def scale(multiplier, input_string):
        pass
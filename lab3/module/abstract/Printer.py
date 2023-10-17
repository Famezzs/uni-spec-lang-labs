from abc import ABC, abstractmethod
    
class Printer(ABC):
    @staticmethod
    @abstractmethod
    def print(output_string):
        pass
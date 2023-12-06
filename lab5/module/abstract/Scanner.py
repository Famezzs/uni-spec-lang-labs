from abc import ABC, abstractmethod
    
class Scanner(ABC):
    @staticmethod
    @abstractmethod
    def scan(prompt='', allow_empty=False):
        pass
from abc import ABC


class ClearsConsole(ABC):
    """
    An abstract marker interface indicating that a class implements functionality to clear the console.

    This interface serves as a contract to ensure that implementing classes provide a method to clear the console. 
    It does not define any methods itself but is used to indicate that the implementing class has this capability.
    """
    pass

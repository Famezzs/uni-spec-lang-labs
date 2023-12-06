from module.static.dedicated_configuration.APIConfiguration import APIConfiguration
from module.static.dedicated_configuration.ExceptionHandlerConfiguration import ExceptionHandlerConfiguration
from module.static.dedicated_configuration.MenuConfiguration import MenuConfiguration

# Class which stores the application's configuration
class Configuration:
    api_configuration = APIConfiguration
    exception_handler_configuration = ExceptionHandlerConfiguration
    menu_configuration = MenuConfiguration
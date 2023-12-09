__all__ = ['Configuration']
from data.shared.configuration.ExceptionHandlerConfiguration import ExceptionHandlerConfiguration
from data.shared.configuration.MenuConfiguration import MenuConfiguration
from data.lab4.module.dedicated_configuration.ArtGeneratorConfiguration import ArtGeneratorConfiguration
from data.lab7.module.dedicated_configuration.APIConfiguration import APIConfiguration
from data.lab8.module.dedicated_configuration.AnalysisConfiguration import AnalysisConfiguration


class Configuration:
    """
    A class that stores the application's configurations.

    This class holds various configuration settings for different components of the application. 
    It is used to centralize the configuration management and make it accessible across the application.

    Attributes:
        exception_handler_configuration: Configuration for the exception handler component.
        menu_configuration: Configuration for the menu component.
        art_generator_configuration: Configuration for the ASCII art generator component.
        api_configuration: Configuration for the API caller component.
        analysis_configuration: Configuration for data analysis component.
        logger: Logger object for logging activities in the application.
    """

    exception_handler_configuration = ExceptionHandlerConfiguration
    menu_configuration = MenuConfiguration
    art_generator_configuration = ArtGeneratorConfiguration
    api_configuration = APIConfiguration
    analysis_configuration = AnalysisConfiguration
    from data.shared.classes.Logger import Logger
    from datetime import datetime
    logger = Logger(f"logs/application-logs-{datetime.now().date()}.log")

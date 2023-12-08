from data.shared.configuration.ExceptionHandlerConfiguration import ExceptionHandlerConfiguration
from data.shared.configuration.MenuConfiguration import MenuConfiguration
from data.lab4.module.dedicated_configuration.ArtGeneratorConfiguration import ArtGeneratorConfiguration
from data.lab7.module.dedicated_configuration.APIConfiguration import APIConfiguration
from data.lab8.module.dedicated_configuration.AnalysisConfiguration import AnalysisConfiguration

# Class which stores the application's configuration
class Configuration:
    exception_handler_configuration = ExceptionHandlerConfiguration
    menu_configuration = MenuConfiguration
    art_generator_configuration = ArtGeneratorConfiguration
    api_configuration = APIConfiguration
    analysis_configuration = AnalysisConfiguration
    from data.shared.classes.Logger import Logger
    from datetime import datetime
    logger = Logger(f"logs/application-logs-{datetime.now().date()}.log")
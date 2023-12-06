from module.APICaller import APICaller
from module.helpers.UserDataFilter import UserDataFilter
from module.helpers.PostDataFilter import PostDataFilter
from module.helpers.CommentDataFilter import CommentDataFilter
from module.helpers.SaveAsFile import SaveAsFile
from module.OutputPrinter import OutputPrinter
from module.InputScanner import InputScanner

# Class which stores the functions called by the Menu class instance
class MenuFunctions:
    @staticmethod
    def __get_color_input():
        scanner = InputScanner(OutputPrinter)
        return scanner.scan('Color: ')
    
    @staticmethod
    def __save_output_as_file(data):
        scanner = InputScanner(OutputPrinter)
        option = scanner.scan('Save to file? (Y/N): ', True) 
        if not option.startswith('y'):
            return
        from tabulate import tabulate
        content = tabulate(data, headers="keys")
        file_name = scanner.scan('File Name: ')
        file_format = scanner.scan('File Format: ')
        SaveAsFile.save_as_file(content, file_name, file_format)

    @staticmethod
    def print_all_users():
        from module.static.Configuration import Configuration
        api_caller = APICaller(Configuration)
        users = api_caller.get_all_users()
        filtered_users = UserDataFilter.filter(users)
        OutputPrinter.print_as_colored_table(filtered_users, MenuFunctions.__get_color_input(), True)
        MenuFunctions.__save_output_as_file(filtered_users)

    @staticmethod
    def print_all_posts():
        from module.static.Configuration import Configuration
        api_caller = APICaller(Configuration)
        posts = api_caller.get_all_posts()
        filtered_posts = PostDataFilter.filter(posts)
        OutputPrinter.print_as_colored_table(filtered_posts, MenuFunctions.__get_color_input(), True)
        MenuFunctions.__save_output_as_file(filtered_posts)

    @staticmethod
    def print_all_comments():
        from module.static.Configuration import Configuration
        api_caller = APICaller(Configuration)
        comments = api_caller.get_all_comments()
        filtered_comments = CommentDataFilter.filter(comments)
        OutputPrinter.print_as_colored_table(filtered_comments, MenuFunctions.__get_color_input(), True)
        MenuFunctions.__save_output_as_file(filtered_comments)

    @staticmethod
    def exit_program():
        exit(0)
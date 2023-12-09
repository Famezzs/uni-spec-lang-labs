import requests

class APICaller:
    """
    A class to handle API calls for retrieving data from specific endpoints.

    This class uses a configuration object to set up API endpoint URLs and provides methods 
    to make GET requests to these URLs.

    Attributes:
        api_url (str): The base URL of the API.
        users_url (str): The URL for accessing user data from the API.
        posts_url (str): The URL for accessing post data from the API.
        comments_url (str): The URL for accessing comment data from the API.

    Methods:
        get_all_users(): Retrieves all users from the API.
        get_all_posts(): Retrieves all posts from the API.
        get_all_comments(): Retrieves all comments from the API.
    """

    def __init__(self, configuration):
        """
        Initializes the APICaller with API endpoint URLs from a given configuration.

        Args:
            configuration: An object containing configuration settings for the API endpoints.
        """
        self.api_url = configuration.api_configuration.api_url
        self.users_url = configuration.api_configuration.users_url
        self.posts_url = configuration.api_configuration.posts_url
        self.comments_url = configuration.api_configuration.comments_url
    
    def get_all_users(self):
        """
        Makes a GET request to the users URL to retrieve all user data.

        Returns:
            list: A list of dictionaries, each representing a user.
        """
        return requests.get(self.users_url).json()
    
    def get_all_posts(self):
        """
        Makes a GET request to the posts URL to retrieve all post data.

        Returns:
            list: A list of dictionaries, each representing a post.
        """
        return requests.get(self.posts_url).json()
    
    def get_all_comments(self):
        """
        Makes a GET request to the comments URL to retrieve all comment data.

        Returns:
            list: A list of dictionaries, each representing a comment.
        """
        return requests.get(self.comments_url).json()
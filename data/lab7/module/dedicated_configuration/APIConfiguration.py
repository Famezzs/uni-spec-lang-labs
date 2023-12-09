class APIConfiguration:
    """
    A configuration class for storing URLs related to an API.

    This class contains class-level attributes that store various URLs used to interact with a specific API. 
    It's designed to centralize and simplify the management of these URLs for the API-related operations.

    Attributes:
        api_url (str): The base URL of the API.
        users_url (str): The URL for accessing user-related data from the API.
        posts_url (str): The URL for accessing post-related data from the API.
        comments_url (str): The URL for accessing comment-related data from the API.
    """
    api_url = 'https://jsonplaceholder.org/'
    users_url = 'https://jsonplaceholder.org/users'
    posts_url = 'https://jsonplaceholder.org/posts'
    comments_url = 'https://jsonplaceholder.org/comments'

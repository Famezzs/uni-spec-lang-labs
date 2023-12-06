import requests

class APICaller:
    def __init__(self, configuration):
        self.api_url = configuration.api_configuration.api_url
        self.users_url = configuration.api_configuration.users_url
        self.posts_url = configuration.api_configuration.posts_url
        self.comments_url = configuration.api_configuration.comments_url
    
    def get_all_users(self):
        return requests.get(self.users_url).json()
    
    def get_all_posts(self):
        return requests.get(self.posts_url).json()
    
    def get_all_comments(self):
        return requests.get(self.comments_url).json()
    
     
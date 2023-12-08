import unittest
from module.APICaller import APICaller
from data.shared.configuration.Configuration import Configuration

class APICallerTests(unittest.TestCase):

    def test_get_all_users_returns_not_none(self):
        api_caller = APICaller(Configuration)
        users = api_caller.get_all_users()
        self.assertIsNotNone(users)
    
    def test_get_all_users_returns_nonempty_result(self):
        api_caller = APICaller(Configuration)
        users = api_caller.get_all_users()
        self.assertTrue(users)

    def test_get_all_posts_returns_not_none(self):
        api_caller = APICaller(Configuration)
        posts = api_caller.get_all_posts()
        self.assertIsNotNone(posts)

    def test_get_all_posts_returns_nonempty_result(self):
        api_caller = APICaller(Configuration)
        posts = api_caller.get_all_posts()
        self.assertTrue(posts)

    def test_get_all_comments_returns_not_none(self):
        api_caller = APICaller(Configuration)
        comments = api_caller.get_all_comments()
        self.assertIsNotNone(comments)
    
    def test_get_all_comments_returns_nonempty_result(self):
        api_caller = APICaller(Configuration)
        comments = api_caller.get_all_comments()
        self.assertTrue(comments)

if __name__ == '__main__':
    unittest.main()

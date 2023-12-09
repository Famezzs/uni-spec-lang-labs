import unittest
from module.APICaller import APICaller
from data.shared.configuration.Configuration import Configuration

class APICallerTests(unittest.TestCase):
    """
    A test suite for testing the APICaller class.

    This class contains a series of unit tests that verify the functionality of the APICaller's methods,
    ensuring that the API calls return data as expected.

    Methods:
        test_get_all_users_returns_not_none(): Tests that the get_all_users method returns a non-none result.
        test_get_all_users_returns_nonempty_result(): Tests that the get_all_users method returns a non-empty result.
        test_get_all_posts_returns_not_none(): Tests that the get_all_posts method returns a non-none result.
        test_get_all_posts_returns_nonempty_result(): Tests that the get_all_posts method returns a non-empty result.
        test_get_all_comments_returns_not_none(): Tests that the get_all_comments method returns a non-none result.
        test_get_all_comments_returns_nonempty_result(): Tests that the get_all_comments method returns a non-empty result.
    """

    def test_get_all_users_returns_not_none(self):
        """
        Tests that the get_all_users method of APICaller returns a result that is not None.
        """
        api_caller = APICaller(Configuration)
        users = api_caller.get_all_users()
        self.assertIsNotNone(users)
    
    def test_get_all_users_returns_nonempty_result(self):
        """
        Tests that the get_all_users method of APICaller returns a non-empty result.
        """
        api_caller = APICaller(Configuration)
        users = api_caller.get_all_users()
        self.assertTrue(users)

    def test_get_all_posts_returns_not_none(self):
        """
        Tests that the get_all_posts method of APICaller returns a result that is not None.
        """
        api_caller = APICaller(Configuration)
        posts = api_caller.get_all_posts()
        self.assertIsNotNone(posts)

    def test_get_all_posts_returns_nonempty_result(self):
        """
        Tests that the get_all_posts method of APICaller returns a non-empty result.
        """
        api_caller = APICaller(Configuration)
        posts = api_caller.get_all_posts()
        self.assertTrue(posts)

    def test_get_all_comments_returns_not_none(self):
        """
        Tests that the get_all_comments method of APICaller returns a result that is not None.
        """
        api_caller = APICaller(Configuration)
        comments = api_caller.get_all_comments()
        self.assertIsNotNone(comments)
    
    def test_get_all_comments_returns_nonempty_result(self):
        """
        Tests that the get_all_comments method of APICaller returns a non-empty result.
        """
        api_caller = APICaller(Configuration)
        comments = api_caller.get_all_comments()
        self.assertTrue(comments)

if __name__ == '__main__':
    unittest.main()
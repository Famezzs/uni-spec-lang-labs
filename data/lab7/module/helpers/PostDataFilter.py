class PostDataFilter:
    """
    A static utility class for filtering post data.

    This class provides a static method to process and filter a list of post data, 
    extracting specific fields and modifying the format as needed.

    Methods:
        filter(posts: list): Takes a list of post dictionaries and returns a filtered version of this list.
    """

    @staticmethod
    def filter(posts: list):
        """
        Filters a list of post dictionaries, extracting and formatting specific fields.

        This method processes each post in the provided list, extracting the 'title', 'category', 'status', 
        and 'publishedAt' fields. The 'title' field is truncated to include only the first 17 characters, 
        followed by an ellipsis.

        Args:
            posts (list): A list of dictionaries, where each dictionary represents a post with at least 'title', 
                          'category', 'status', and 'publishedAt' keys.

        Returns:
            list: A list of dictionaries with filtered and formatted post data. Each dictionary contains 'Title', 
                  'Category', 'Status', and 'Publish Date' keys.
        """
        filtered_posts = list()
        for post in posts:
            filtered_posts.append({
                'Title': post['title'][0:17] + '...',
                'Category': post['category'],
                'Status': post['status'],
                'Publish Date': post['publishedAt']
            })
        return filtered_posts

class PostDataFilter:
    @staticmethod
    def filter(posts: list):
        filtered_posts = list()
        for post in posts:
            filtered_posts.append({
                'Title': post['title'][0:17] + '...',
                'Category': post['category'],
                'Status':  post['status'],
                'Publish Date': post['publishedAt']
            })
        return filtered_posts
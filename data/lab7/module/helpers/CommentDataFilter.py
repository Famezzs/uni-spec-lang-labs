class CommentDataFilter:
    @staticmethod
    def filter(comments: list):
        filtered_comments = list()
        for comment in comments:
            filtered_comments.append({
                'User Id': comment['userId'],
                'Content': comment['comment'][0:34] + '...',
            })
        return filtered_comments
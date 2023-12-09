class UserDataFilter:
    """
    A utility class for filtering user data.

    Provides a static method to process and filter a list of user data dictionaries, extracting 
    specific fields and restructuring the data format.

    Methods:
        filter(users: list): Filters a list of user data dictionaries based on specific fields.
    """

    @staticmethod
    def filter(users: list):
        """
        Filters a list of user data dictionaries, extracting specific fields: 'First Name', 'Last Name', 
        'Email', and 'Birth Date'.

        Args:
            users (list): A list of dictionaries, where each dictionary contains data about a user.

        Returns:
            list: A list of dictionaries with filtered user data. Each dictionary includes 'First Name', 
                  'Last Name', 'Email', and 'Birth Date' fields.
        """
        filtered_users = list()
        for user in users:
            filtered_users.append({
                'First Name': user['firstname'],
                'Last Name': user['lastname'],
                'Email': user['email'],
                'Birth Date': user['birthDate']
            })
        return filtered_users

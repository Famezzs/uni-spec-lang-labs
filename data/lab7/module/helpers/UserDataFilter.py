class UserDataFilter:
    @staticmethod
    def filter(users: list):
        filtered_users = list()
        for user in users:
            filtered_users.append({
                'First Name': user['firstname'],
                'Last Name': user['lastname'],
                'Email':  user['email'],
                'Birth Date': user['birthDate']
            })
        return filtered_users
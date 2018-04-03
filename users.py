import pyperclip

class Users:
    """
    This class generates new instances of users
    """
    users_list = []

    def __init__(self, first_name, last_name, password):
        """
        __init__ method defines our object.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_users(self):
        """
        save_users saves our users objects into users_list
        """

        Users.users_list.append(self)

    def delete_users(self):
        """
        delete_users method deletes saved users from the users_list.
        """
        Users.users_list.remove(self)

    @classmethod
    def find_by_first_name(cls, first_name):

        for users in cls.users_list:
            if users.first_name == first_name:
                return users

    @classmethod
    def users_exist(cls, first_name):
        for users in cls.users_list:
            if users.first_name == first_name:
                return True
        return False

    @classmethod
    def display_users(cls):
        return cls.users_list

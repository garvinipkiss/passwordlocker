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
#
        Users.users_list.append(self)

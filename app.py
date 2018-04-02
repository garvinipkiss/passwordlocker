#usr/bin/env python3.6 app.py
import pyperclip
import random
"""
1.Generate password
2.Save password
3.Tear Down
4.Save multiple accounts
5.Delete several password accounts
6.Find accounts
7.Display accounts
8.Copy_paste
"""
# import random users credentials

""""
Our application we will need only:
1. Accounts - different accounts for users.
2. Passwords - able to save different accounts Passwords.
"""


class Users:
    def __init__(self, first_name, last_name, Accounts_key):
        self.first_name = first_name
        self.last_name = last_name
        self.Accounts_key = Accounts_key


class Passwords:
    """
    This class will generate new instances of accounts.
    Below we create a class variable,password_list[]
    this will be able to store our passwords and different accounts info as a list.
    """
    password_list = []

    def __init__(self, account_name, account_password, password_length):
        """
        The init method creates new instances of our class and passes in properties for the object.

        """

        self.account_name = account_name
        self.account_password = account_password
        self.password_length = password_length

    def save_account(self):
        """
        We create our save account function that will append every account
        and passwords .
        """
        Passwords.password_list.append(self)

    """
    Below we encounter decorators in python.
    They basically allow us to make simple modifications to callable objects
    like functions, methods, or classes

    Here we want to allow some of our functions to apply to the entire class.
    """

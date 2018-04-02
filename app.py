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

@classmethod
    def Accounts_exists(cls, account_name):
        """
        This are python decorators they check if an account exists from password_list and takes in the name and returns a boolean if the matching account is found.
        """
        for Accounts in cls.password_list:
            if Accounts.account_name == account_name:
                return True
        return False

    @classmethod
    def display_Accounts(cls):
        """
        This method returns different account list.
        """
        return cls.password_list

    @classmethod
    def find_by_account(cls, account_name):
        """
        This method takes in an account name and returns the password matching
        the account.
        """
        for Accounts in cls.password_list:
            if Accounts.account_name == account_name:
                return profile

    @classmethod
    def copy_passwords(cls, account_name):
        password_found = Passwords.find_by_account(account_name)
        pyperclip.copy(password_found.account_password)

    @classmethod
    def password_gen(cls, password_length):
        string = "abcdefghigjkmnopqrstuvwxyz1234567890-_=+%[]{}\|"'?:;>./,`!@#$^&*()`'"
        password = "".join(random.sample(string, int(password_length)))
        accounts_passsword = password
        return accounts_passsword

# print("Choose more than eight characters with numbers and asterics")
# password_length = int(input())
# string = "abcdefghigjkmnopqrstuvwxyz1234567890-_=+%[]{}\|"'?:;>./,`!@#$^&*()`"
# password = "".join(random.sample(string, password_length))
# print(password)

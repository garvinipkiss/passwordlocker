#usr/bin/env python3.6
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



class User:

    user_list = []

    def __init__(self, locker_userName, locker_password):

        self.locker_userName = locker_userName
        self.locker_password = locker_password

    def save_user(self):
        User.user_list.append(self)

    # @classmethod
    # def find_by_account_name(cls, account_name)
    #     for user in cls.user_list:
    #         if user.locker_userName == account_name:
    #             return user


class Password:

    password_list =[]

    def __init__(self,account_name,user_name,email,account_password):


        self.account_name = account_name
        self.user_name = user_name
        self.email = email
        self.account_password = account_password

    def save_password(self):
        Password.password_list.append(self)

    def delete_password(self):
        Password.password_list.remove(self)

    @classmethod
    def find_by_account_name(cls,account_name):
            for password in cls.password_list:
                if password.account_name == account_name:
                    return password

    @classmethod
    def password_exist(cls,account_name):
        for password in cls.password_list:
            if password.account_name == account_name:
                return True
        return False

    @classmethod
    def display_password(cls):
        return cls.password_list

    @classmethod
    def copy_user_name(cls,user_name):
        password_found = Password.find_by_account_name(user_name)
        pyperclip.copy(password_found.account_password)

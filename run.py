#!/usr/bin/env python3.6
from app import Passwords
from users import Users
import random

"""
Users Details
"""


def create_users(fname, lname, password):
    """
    We create the new users_list.
    """
    new_users = Users(fname, lname, password)
    return new_users


def save_users(users):
    """
    This function saves users.
    """
    user.save_users()


def del_users(users):
    """
    This function work is to delete users.
    """
    users.delete_users()


def find_users(number):
    """
    This function finds users by numbers and returns the results.
    """
    return Users.find_by_number(number)


def check_existing_users(number):
    """
    check_existing_users function checks if the users exists with that number and return Boolean
    """
    return Users.users_exist(number)


def display_users():
    """
    This function displays users.
    """
    return Users.display_users()


def copy_password(number):
    """
    This function copys passwords.
    """
    return Users.copy_password()


def create_Accounts(account_name, account_password, password_length):
    """
    This function creates new_accounts
    """
    new_Accounts = Passwords(account_name, account_password, password_length)
    return new_Accounts


def save_Accounts(account):

    Accounts.save_account()


def find_Accounts(account_name):
    """
    This function finds accounts passswords
    """
    return Passwords.find_by_accounts(account_name)


def Accounts_exists(account_name):
    """
    This function check if an account exists and returns a
    boolean if found or not.
    """
    return Passwords.Accounts_exists(account_name)


def display_Accounts():
    """
    This function displays all saved accounts
    """
    return Passwords.display_Accounts()


def copy_password(account_name):
    """
    This function copys passwords.
    """
    return Passwords.copy_password()


def password_gen(password_length):
    return Passwords.password_gen(password_length)


def main():
    print("Hi! ")
    user_name = input()
    print("")

    print(f"Hi {user_name}. ?")
    print("")

    while True:
        print("""Use the following keys :
              create - create new account
              log in - log in to your password profiles
              log out - log out of you account
              exit - exit account list.""")
        short_code = input().lower()
        print("_" * 100)
        if short_code == "create":
            print("New PasswordLocker Account")
            print("_" * 20)

            print("Enter first name -")
            f_name = input()

            print("Enter last name -")
            l_name = input()

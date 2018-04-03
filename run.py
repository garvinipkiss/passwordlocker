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
    print("""
                  We can generate a password for you. Use the following keys:
                  generate- to generate a password
                  open- to create your own password.
                  """)
            pass_code = input().lower()
            print("__" * 20)
            if pass_code == "generate":
                password_length = int(
                    input("create a strong length of your own "))
                password = password_gen(password_length)
                print(f"Your new password is {password}")
            else:
                print("Write a password that we will save for you")
                password = input()

            save_users(create_user(f_name, l_name, password))

            print("")
            print(
                f"""New account created for - {f_name} {l_name} your account password is - {password}""")
            print("")
            print("Use a good password")
        while True:
            print("""Use the following keys:
                  creates - create password account,
                  display - displays accounts,
                  find - find a password account,
                  exit - exit account list.""")
            short_code = input().lower()
            print("_" * 100)
            if key == "creates":
                print(
                    "Which accounts do you want to save a password for? Eg Emails, social media, ")
                account_name = input()
                print("""
                      We can generate a passwords for you. Use the following keys:
                      generate- to generate a password
                      open- to create your own password.
                      """)
                pass_code = input().lower()
                print("__" * 20)
                if pass_code == "generate":

    password_length = int(
                        input("How long do you want your password - "))

                    password = password_gen(password_length)
                    print("")
                    print(f"Your password for this {account_name} is: {password}")
                    print("")
                    print("__" * 20)
                else:
                    print("Write a password of your own. We'll store it for you")
                    password = input()
                    password_length = len(password)
                    print("")
                    print(f"Your password for this {account_name} is: {password}")
                    print("")
                    print("__" * 20)

                save_Accounts(create_account(
                    account_name, password, password_length))

            elif key == "display":
                if display_Accounts():
                    print("Your various accounts")
                    print("")
                    for Accounts in display_accounts():
                        print(
                            f"Account- {Accounts.account_name}, Password- {Accounts.account_password}, Password Length- {Accounts.password_length}")
                        print("")
                else:
                    print("")
                    print("No account is yet saved")
                    print("")

            elif key == "find":
                print("in order to view your accounts password enter the accounts name")

                account_name = input()
                if Accounts_exists(account_name):
                    search_Accounts = find_Accounts(account_name)
                    print("_" * 20)
                    print(f"{search_Accounts.account_name}")
                    print(f"Password - {search_Accounts.account_password}")
                    print("")
                    print(
                        f"Password Length - {search_account.password_length}")
                    print("_" * 20)
                else:
                    print("This account doesn't exist")
                    print("")

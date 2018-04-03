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

#!/usr/bin/env python3.6
import unittest
import pyperclip
import string
import random

from app_locker import User, Credentials


class TestUser(unittest.TestCase):
    """
    Test that defines test cases for the user class bevaviours
    """
    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_user = User("Berserk", "0000", "garvinipkiss@gmail.com")
    def test_init(self):
        """
        Test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.user_name,"Berserk")
        self.assertEqual(self.new_user.password, "0000")
        self.assertEqual(self.new_user.email, "garvinipkiss@gmail.com")

    def tearDown(self):
        """
        Method that cleans up after each case has run.
        """
        User.user_list = []

    def test_user_save(self):
        """
        Test case to test if the user object is saved into the user_list.
        """
        self.new_user.user_save()

        self.assertEqual(len(User.user_list),1)
    def test_save_multiple_user(self):
        """
        Test to check whether we can save multiple user objects.
        """
        self.new_user.user_save()
        test_user = User("ninja","0000","ninja@gmail.com")
        test_user.user_save()
        self.assertEqual(len(User.user_list),2)

    def test_display_users(self):
        self.assertEqual(User.display_users(),User.user_list)

class TestCredentials(unittest.TestCase):
    """
    Test that define test cases for credentials.
    """
    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_credential = Credentials("Berserk","ninja", "Garvin")

    def test_init(self):
        """
        Test case to test if the object is initialized properly.
        """

        self.assertEqual(self.new_credential.account_name,"Berserk")
        self.assertEqual(self.new_credential.account_username,"ninja")
        self.assertEqual(self.new_credential.account_password,"Garvin")

    # def test_user_login(self):
    #     """
    #     Test case to test if we can find a user by password.
    #     """
    #     self.new_user.user_save()
    #     test_user = User("ninja","0000","ninja@gmail.com")
    #     test_user.user_save()
    #     found_user = User.user_login("0000")

    #     self.assertEqual(found_user.password,test_user.password)

    def tearDown(self):
        Credentials.credential_list = []
    # def test_check_user_exist(self):
    #     """
    #     test case to test if a user exists, returns true if a user exists,otherwise false.
    #     """
    #     self.User.new_user.user_save()
    #     test_user = User("Berserk", "0000", "garvinipkiss@gmail.com")
    #     test_user.user_save()
    #     user_exist = User.user_exist("0000")

    #     self.assertTrue(user_exist)

    def test_save_account(self):
        """
        Test case to test if the credential object is saved in to credential_list.
        """
        self.new_credential.save_account()
        self.assertEqual(len(Credentials.credential_list), 1)

    def test_save_multiple_account(self):
        """
        Test case to test if we can save multiple credential objects.
        """
        self.new_credential.save_account()
        test_account = Credentials("linkedin","Garvin","Berserk")
        test_account.save_account()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_account(self):
        """
        Test case to test if we can remove an account from credential list.
        """
        self.new_credential.save_account()
        test_credential = Credentials("Berserk","linkedin","Garvin")
        test_credential.save_account()

        self.new_credential.delete_account()

        self.assertEqual(len(Credentials.credential_list),1)

    def test_display_accounts(self):
        """
        Test case to test if lists of accounts are displayed.
        """
        self.assertEqual(Credentials.display_accounts(),Credentials.credential_list)

if __name__ == '__main__':
  unittest.main(verbosity = 2)

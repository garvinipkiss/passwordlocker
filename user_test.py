#!/usr/bin/env python3.6
import unittest
from app import Passwords
import pyperclip


class TestPasswords(unittest.TestCase):

    def setUp(self):
        """
        setUp() method defines instructions that are
        executed before each test method.
        We then store it as an instance variable in the test class as:
        self.new_password
        """

        self.new_Accounts = Passwords("Madthings", "shortgun", "lost")

    def tearDown(self):
        """
        This cleans up after every test case.
        """
        Passwords.password_list = []

    def test_instance(self):
        """
        test_instance tests if the object created in setUp is initialized or has been instanciated properly.
        """

        self.assertEqual(self.new_Accounts.account_name, "Madthings")
        self.assertEqual(self.new_Accounts.account_password,
                         "shortgun")
        self.assertEqual(self.new_Accounts.password_length,
                         "lost")

    def test_save_Accounts(self):

        self.new_Accounts.save_account()
        self.assertEqual(len(Passwords.password_list), 1)

        def test_save_multiple_Accounts(self):
        """
        This function can save multiple contacts.
        """
        test_Accounts = Passwords("Facebook", "newfacebookuser", "20")
        """
        We create our save_account function that will append every account and passwords.
        """
        test_Accounts.save_account()
        self.new_Accounts.save_account()
        self.assertEqual(len(Passwords.password_list), 2)

    def test_find_by_account(self):
        """
        Test to check if we can find our passwords by account and display.
        """
        test_Accounts = Passwords("Facebook", "newfacebookuser", "20")
        test_Accounts.save_account()
        """
        We create our save_account function that will append every account and passwords.
        """
        found_profile = Passwords.find_by_account("Facebook")
        self.new_Accounts.save_account()
        self.assertEqual(found_Accounts.account_password,
                         test_Accounts.account_password)

    def test_Accounts_exists(self):
        """
        Checks if we can return a boolean if we cannot find an account.
        """

        self.new_Accounts.save_account()
        test_Accounts = Passwords("Facebook", "newfacebookuser", "20")
        test_Accounts.save_account()

        test_exists = Passwords.account_exists("Facebook")
        self.assertTrue(test_exists)

def test_display_Accounts(self):
        """
        This function displays a list of all the accounts saved.
        """
        self.assertEqual(Passwords.display_profiles(), Passwords.password_list)

    def test_copy_password(self):
        """
        This function copys the password from an account.
        """
        self.new_Accounts.save_account()
        Passwords.copy_password("Madthings")

        self.assertEqual(self.new_Accounts.account_password, pyperclip.paste())

    def test_password_gen(self):
        """
        We test if our password generator works.
        """
        self.new_Accounts.save_account()
        random_password = self.new_Accounts.password_gen("lost")
        self.assertNotEqual(random_password, self.new_Accounts.account_password)


if __name__ == "__main__":
    unittest.main()

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
        

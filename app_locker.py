#usr/bin/env python3.6 app.py
import pyperclip
import random
import string

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

# user_name =""
# user_password =""
global user_list
class User:
  """
  Class that generates new instances of user
  """

  user_list = [] #empty user list
  def __init__(self, user_name, password,email):
    self.user_name = user_name
    self.password = password
    self.email = email

  def user_save(self):
    """
    saves user object into user object.
    """
    User.user_list.append(self)
  @classmethod
  def display_users(cls):
    return cls.user_list


class Credentials:
  """
  Class that generates new instances of credential object.
  """
  global user_list
  credential_list =[]
  def __init__(self, account_name, account_username, account_password):
    self. account_name = account_name
    self.account_username = account_username
    self.account_password = account_password
  @classmethod
  def check_user_exist(cls,user_name,password):
    """
    Method that checks if a user exist from user list.
    """
    for user in User.user_list:
      if user.user_name == user_name and user.password == password:
        return True
      return False



  # @classmethod
  # def user_login(cls,password):
  #   for user in cls.user_list:
  #     if User.user_list.password == password:
  #       return Credentials.credential_list

  def save_account(self):
    """
    save_account saves credential object into credential object.
    """
    Credentials.credential_list.append(self)

  def delete_account(self):
    """
    delete_account method removes a saved cretential from credential list.
    """
    Credentials.credential_list.remove(self)

  @classmethod
  def display_accounts(cls):
    """
    Method that returns the credential list.
    """
    return cls.credential_list
  def generate_password():
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"

    gen_pass = "".join(random.choice(char) for _ in range(8))

    return gen_pass

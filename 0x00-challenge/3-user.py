#!/usr/bin/python3
"""
User Model
"""
import hashlib
import uuid


class User():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, hashed_password):
        if isinstance(hashed_password, str):
            self.__password = hashed_password
        else:
            self.__password = None

    def is_valid_password(self, plain_password):
        if not isinstance(plain_password, str) or self.__password is None:
            return False
        return self.__password == plain_password

if __name__ == '__main__':
    print("Test User")

    user_1 = User()
    if user_1.id is None:
        print("New User should have an id")

    user_2 = User()
    if user_1.id == user_2.id:
        print("User.id should be unique")

    u_pwd = hashlib.sha256(b"myPassword").hexdigest()
    user_1.password = u_pwd
    if user_1.password == u_pwd:
        print("User.password should be hashed")

    if user_2.password is not None:
        print("User.password should be None by default")

    user_2.password = None
    if user_2.password is not None:
        print("User.password should be None if setter to None")

    user_2.password = 89
    if user_2.password is not None:
        print("User.password should be None if setter to an integer")

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True if it's the right password")

    if user_1.is_valid_password(hashlib.sha256(b"Fakepwd").hexdigest()):
        print("is_valid_password should return False if it's not the right password")

    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compare with None")

    if user_1.is_valid_password(89):
        print("is_valid_password should return False if compare with integer")

    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password set before")

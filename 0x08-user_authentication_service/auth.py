#!/usr/bin/env python3
"""4. Hash password """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """return a User object"""
        try:
            find = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hash_pwd = _hash_password(password)
            return self._db.add_user(email, hash_pwd)

    def valid_login(self, email: str, password: str) -> bool:
        """Try locating the user. If it exists, check the password
        If it matches return True. Otherwise, return False."""
        try:
            find = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), find.hashed_password):
                return True
        except NoResultFound:
            return False
        return False


def _hash_password(password: str) -> str:
    """returned bytes is a
    salted hash of the input password"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """return a string representation of a new UUID"""
    return str(uuid4())

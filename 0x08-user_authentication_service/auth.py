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

    def create_session(self, email: str) -> str:
        """returns the session ID as a string"""
        try:
            find = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(find.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return

    def get_user_from_session_id(self, session_id: str) -> User:
        """returns the corresponding User or None"""
        if session_id is None:
            return None
        try:
            find = self._db.find_user_by(session_id=session_id)
            return find
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """Destroy session """
        try:
            find = self._db.find_user_by(id=user_id)
            user_data = {"session_id": None}
            self._db.update_user(find.id, **user_data)
        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """generate a UUID and update the user’s reset_token"""
        try:
            find = self._db.find_user_by(email=email)
            if find:
                self._db.update_user(find.id, reset_token=_generate_uuid())
                return find.reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """update the user’s hashed_password """
        try:
            find = self._db.find_user_by(reset_token=reset_token)
            if find:
                password = _hash_password(password)
                data = {'hashed_password': password,
                        'reset_token': None}
                self._db.update_user(find.id, **data)
        except NoResultFound:
            raise ValueError
        return None


def _hash_password(password: str) -> str:
    """returned bytes is a
    salted hash of the input password"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """return a string representation of a new UUID"""
    return str(uuid4())

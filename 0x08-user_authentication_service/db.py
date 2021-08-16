#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """returns a User object that should save the user to the database."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """returns the first row found in the users table"""
        if not kwargs:
            return InvalidRequestError
        users = [
            'id', 'email', 'hashed_password',
            'session_id', 'reset_token']
        for item in kwargs:
            if item not in users:
                raise InvalidRequestError
        search = self.__session.query(User).filter_by(**kwargs).first()
        if search:
            return search
        else:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """The method will use find_user_by
        to locate the user to update"""
        find = self.find_user_by(id=user_id)
        users = [
            'id', 'email', 'hashed_password',
            'session_id', 'reset_token']
        for key, val in kwargs.items():
            if key in users:
                setattr(find, key, val)
            else:
                raise ValueError
        self._session.commit()

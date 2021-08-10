#!/usr/bin/env python3
"""class SessionAuth that inherits from Auth"""

from logging import NOTSET

from flask.globals import session
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """class SessionAuth that
    inherits from Auth"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id.update({session_id: user_id})
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns a User instance based on a cookie value"""
        session_id = self.session_cookie(request)
        return User.get(self.user_id_for_session_id(session_id))

    def destroy_session(self, request=None):
        """deletes the user session / logout"""
        if request is None:
            return False
        if not self.session_cookie(request):
            return False
        session_id = self.session_cookie(request)
        if not self.user_id_for_session_id(session_id):
            return False
        self.user_id_by_session_id.pop(session_id)
        return True

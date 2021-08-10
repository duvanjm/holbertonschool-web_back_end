#!/usr/bin/env python3
"""class SessionAuth that inherits from Auth"""

from uuid import uuid4
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """class SessionAuth
    that inherits from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create
        s a Session ID for a user_id"""
        if user_id == None:
            return None
        if type(user_id) is not str:
            return None
        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id

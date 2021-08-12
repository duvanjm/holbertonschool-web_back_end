#!/usr/bin/env python3
"""class SessionExpAuth that
inherits from SessionAuth"""

from flask.globals import session
from api.v1.auth.session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """class SessionExpAuth that
    inherits from SessionAuth"""

    def __init__(self):
        """init method"""
        self.session_duration = 0
        if int(os.getenv('SESSION_DURATION')):
            self.session_duration = int(os.getenv('SESSION_DURATION'))

    def create_session(self, user_id=None):
        """Create a Session ID by calling super()
        Return None if super() can’t create a Session ID"""
        try:
            session_id = super().create_session(user_id)
        except Exception:
            return None
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """return user_id from the session dictionary"""
        if session_id is None:
            return None
        if session_id not in self.user_id_for_session_id:
            return None
        if self.session_duration == 0:
            return self.user_id_for_session_id.get('user_id')
        if self.created_at not in self.user_id_for_session_id:
            return None
        created = self.user_id_for_session_id.get('created_at')
        time_delta = timedelta(seconds=self.session_duration)
        if created + time_delta < datetime.now():
            return None
        return self.user_id_for_session_id.get('user_id')

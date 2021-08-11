#!/usr/bin/env python3
"""Auth class """

from flask import request
import os
from typing import TypeVar, List


class Auth():
    """Auth class to manage
    the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path"""
        if path is None or excluded_paths is None:
            return True
        if len(excluded_paths) == 0:
            return True
        if path[-1:] != '/':
            path = path + '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None - request"""
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        if os.getenv('SESSION_NAME'):
            return request.cookies.get('_my_session_id')

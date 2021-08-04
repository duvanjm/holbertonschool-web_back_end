#!/usr/bin/env python3
"""class Basic auth"""

from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """class BasicAuth that inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> str:
        """returns the Base64 part of
        the Authorization header for
        a Basic Authentication"""
        if authorization_header is None:
            return None
        if isinstance(authorization_header, str) is False:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """returns the decoded value of
        a Base64 string base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        if isinstance(base64_authorization_header, str) is False:
            return None
        try:
            message = base64_authorization_header.encode('utf-8')
            dcode = base64.b64decode(message)
            return dcode.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """returns the user email and
        password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if isinstance(decoded_base64_authorization_header, str) is False:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        data = decoded_base64_authorization_header.split(':', 1)
        return data[0], data[1]

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the User
        instance based on his email and password"""
        if isinstance(user_email, str) is False:
            return None
        if isinstance(user_pwd, str) is False:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for pwd in users:
            if pwd.is_valid_password(user_pwd):
                return pwd
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves the User instance for a request"""
        autorization = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(autorization)
        decod = self.decode_base64_authorization_header(b64)
        user, pwd = self.extract_user_credentials(decod)
        return self.user_object_from_credentials(user, pwd)

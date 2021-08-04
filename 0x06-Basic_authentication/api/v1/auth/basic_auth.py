#!/usr/bin/env python3
"""Basic auth"""

from api.v1.auth.auth import Auth
import base64
import split


class BasicAuth(Auth):
    """class BasicAuth that inherits from Auth"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
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

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
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
        except:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and
        password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None
        if isinstance(decoded_base64_authorization_header, str) is False:
            return None
        if ':' not in decoded_base64_authorization_header:
            return None
        data = decoded_base64_authorization_header.split(':', 1)
        return data[0], data[1]

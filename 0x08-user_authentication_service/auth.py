#!/usr/bin/env python3
"""4. Hash password """

import bcrypt


def _hash_password(password) -> bytes:
    """returned bytes is a
    salted hash of the input password"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

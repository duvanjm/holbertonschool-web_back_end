#!/usr/bin/env python3
"""main file to test flask application"""

import requests


def register_user(email: str, password: str) -> None:
    """test registes user end point"""
    user = {'email': email, 'password': password}
    req = requests.post('http://0.0.0.0:5000/users', user)
    assert req.status_code == 200

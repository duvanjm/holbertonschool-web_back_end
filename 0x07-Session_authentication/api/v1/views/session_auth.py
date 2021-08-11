#!/usr/bin/env python3
"""Flask view that handles
all routes for the Session
authentication"""

from flask import Flask, request, jsonify, abort
from api.v1.views import app_views
import os
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """handles all routes for the Session authentication"""
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400
    if password is None or len(password) == 0:
        return jsonify({"error": "password missing"}), 400

    try:
        search = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not search:
        return jsonify({"error": "no user found for this email"}), 404
    for user in search:
        if user.is_valid_password(password) is True:
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            cookie = os.getenv('SESSION_NAME')
            responce = jsonify(user.to_json())
            responce.set_cookie(cookie, session_id)
            return responce
        else:
            return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """deletes the user session / logout"""
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    else:
        return jsonify({}), 200

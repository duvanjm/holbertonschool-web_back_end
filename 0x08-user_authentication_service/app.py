#!/usr/bin/env python3
"""set up a basic Flask app"""

from flask import Flask, jsonify, request, abort, redirect
from flask.helpers import url_for
from werkzeug.wrappers import response
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def message() -> str:
    """return a JSON payload"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def register() -> str:
    """end-point to register a user."""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """create a new session for the user"""
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password) is False:
        abort(401)
    else:
        try:
            sesion_id = AUTH.create_session(email)
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('sesion_id', sesion_id)
            return response
        except Exception:
            return None


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> None:
    """destroy the session and redirect the user to GET /"""
    session_id = request.cookies.get('session_id')
    if session_id:
        user_id = AUTH.get_user_from_session_id(session_id)
        if user_id:
            AUTH.destroy_session(user_id.id)
            return redirect(url_for('index'))
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

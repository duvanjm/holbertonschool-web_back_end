#!/usr/bin/env python3
"""set up a basic Flask app"""
from auth import Auth
from flask import abort, Flask, jsonify, redirect, request
from flask.helpers import make_response
from sqlalchemy.orm.exc import NoResultFound
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
        sesion_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"}), 200
        response.set_cookie('sesion_id', sesion_id)
        return response


@app.route('/sessions', methods=["DELETE"])
def logout():
    """destroy the session and redirect the user to GET /"""
    session_id = request.cookies.get('session_id')
    if session_id is not None:
        user = AUTH.get_user_from_session_id(session_id)
        if user is not None:
            AUTH.destroy_session(user.id)
            return redirect('/')
    return abort(403)


@app.route('/profile')
def profile():
    """if user exists retunr 200 http status"""
    session_id = request.cookies.get('session_id')
    if session_id is not None:
        user = AUTH.get_user_from_session_id(session_id)
        if user is not None:
            return jsonify({"email": user.email}), 200
    return abort(403)


@app.route('/reset_password', methods=['POST'])
def reset_pwd():
    """respond to the POST /reset_password route."""
    email = request.form.get('email')
    try:
        find = AUTH._db.find_user_by(email=email)
        if find:
            token = AUTH.get_reset_password_token(email)
            return jsonify({"email": email, "reset_token": token}), 200
    except NoResultFound:
        return None


@app.route('/reset_password', methods=['PUT'])
def reset_passwd():
    """Update the password"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        return abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

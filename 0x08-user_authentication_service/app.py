#!/usr/bin/env python3
"""Set up a basic Flask app"""
from auth import Auth
from flask import Flask, jsonify, request, abort, redirect, make_response
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """root route"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def register():
    """ end-point to register a new user. """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ login, create a new session for the user """
    email = request.form.get('email')
    password = request.form.get('password')

    valid_cred = AUTH.valid_login(email=email, password=password)
    if valid_cred:
        session_id = AUTH.create_session(email)
        response = make_response({"email": "email",
                                  "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    abort(401)


@app.route('/sessions', methods=["DELETE"])
def logout():
    """ destry session, logout """
    session_id = request.cookies.get('session_id')
    if session_id is not None:
        user = AUTH.get_user_from_session_id(session_id)
        if user is not None:
            AUTH.destroy_session(user.id)
            return redirect('/')
    return abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """ End point to acces user's profile
    methods GET arguments None
    User profile """
    session_id = request.cookies.get('session_id')
    if session_id is not None:
        user = AUTH.get_user_from_session_id(session_id)
        if user is not None:
            return jsonify({"email": user.email}), 200
    return abort(403)


@app.route('/reset_password', methods=['POST'])
def reset_pwd():
    """ respond to the POST /reset_password route. """
    email = request.form.get('email')
    try:
        find = AUTH._db.find_user_by(email=email)
        if find:
            token = AUTH.get_reset_password_token(email)
            return jsonify({"email": email, "reset_token": token}), 200
    except NoResultFound:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def reset_passwd():
    """ Update the user's password """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH._db.find_user_by(email=email)
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

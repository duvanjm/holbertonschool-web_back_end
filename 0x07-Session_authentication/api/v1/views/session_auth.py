#!/usr/bin/env python3
"""Flask view that handles
all routes for the Session
authentication"""

from flask import Flask, request, jsonify, abort
from api.v1.views import app_views
import os
from models.user import User


@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """deletes the user session / logout"""
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    else:
        return jsonify({}), 200

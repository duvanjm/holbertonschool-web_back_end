#!/usr/bin/env python3
"""set up a basic Flask app"""

from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def message() -> str:
    """return a JSON payload"""
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

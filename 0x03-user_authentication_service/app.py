#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify
from requests import request
from auth import Auth
from typing import Union

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def status() -> str:
    """ GET /status
    Return:
      - JSON payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register() -> Union[str, tuple]:
    """
        register user route
        """
    email = request.form["email"]
    password = request.form["password"]
    try:
        Auth.register_user(email, password)
        return jsonify({
            "email": email,
            "message": "user created"
        })
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="7000")

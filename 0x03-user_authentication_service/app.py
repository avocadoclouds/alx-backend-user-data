#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify, request, abort, redirect
from typing import Union
from auth import Auth


AUTH = Auth()
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
        AUTH.register_user(email, password)
        return jsonify({
            "email": email,
            "message": "user created"
        })
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

# Task 11


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Returns a boolean by checking the email & password."""
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie('session_id', session_id)
    return res


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Finds the user with the requested session ID.
    Deletes User by using session_id.
    Then, redirects to GET /.
    If no user exits, respond with a 403 HTTP status.
    """
    user_cookie = request.cookies.get("session_id", None)
    user = AUTH.get_user_from_session_id(user_cookie)
    if user_cookie is None or user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def get_profile():
    """
    Respond to the GET /profile route.
    Request should contain a session_id cookie, which
    will be used to find the user.
    If the user exist, respond with a 200 HTTP status.
    If the session ID is invalid or the user does not exist,
    respond with a 403 HTTP status.
    """

    user_cookie = request.cookies.get("session_id", None)
    if user_cookie is None:
        abort(403)
    user = AUTH.get_user_from_session_id(user_cookie)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="7000")

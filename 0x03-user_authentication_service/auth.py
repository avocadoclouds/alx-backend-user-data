#!/usr/bin/env python3
""" Auth Model"""

import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from user import User
from db import DB
from uuid import uuid4

# Private functions to the auth modeule and not be used outside of it


def _hash_password(password: str) -> bytes:
    """
    Returns Bytes,
    Takes a password as an argument and hashes it
    """

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """Returns a string representation of a new UUID"""
    UUID = uuid4()
    return str(UUID)

# class Auth and its methods


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Returns a new user, if email is used it raises value error
        if not, the password is hashed and saved to db
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)

            return user

        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """If password is valid returns true, else, false"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        user_password = user.hashed_password
        encoded_password = password.encode()

        if bcrypt.checkpw(encoded_password, user_password):
            return True

        return False

    def create_session(self, email: str) -> str:
        """ Returns session ID for a user """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()

        self._db.update_user(user.id, session_id=session_id)

        return session_id

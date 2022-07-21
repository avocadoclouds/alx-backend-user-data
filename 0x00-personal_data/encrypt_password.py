#!/usr/bin/env python3
"""encrypt passwords with bcrypt"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    expects one string argument name password and returns a salted,
    hashed password, which is a byte string.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

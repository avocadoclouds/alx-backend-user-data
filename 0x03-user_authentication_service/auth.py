#!/usr/bin/env python3
""" Auth Model"""

from asyncio.events import BaseDefaultEventLoopPolicy
import bcrypt
from user import User
from db import DB


def _hash_password(password: str) -> bytes:
    """
    Returns Bytes,
    Takes a password as an argument and hashes it
    """

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

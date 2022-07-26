#!/usr/bin/env python3
""" a class to manage the API authentication."""
from flask import request
from typing import List, TypeVar


class Auth:
    """manages API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        return False for now
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        returns None
        request - Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None
        request - Flask request object
        """

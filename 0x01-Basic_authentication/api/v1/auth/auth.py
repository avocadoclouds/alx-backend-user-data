#!/usr/bin/env python3
""" a class to manage the API authentication."""
from flask import request
from typing import List, TypeVar


class Auth:
    """manages API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns True if the path is not in the
        list of strings excluded_paths:
            Returns True if path is None
            Returns True if excluded_paths is None or empty
            Returns False if path is in excluded_paths
        """

        if excluded_paths is None or []:
            return True
        if path is None:
            return True
        if path in excluded_paths or path[-1] != '/' and path + '/'\
                in excluded_paths:
            # slash tolerant
            return False

        return True

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

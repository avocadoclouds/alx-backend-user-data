#!/usr/bin/env python3
""" BasicAuth that inherits from Auth """

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Inherits from Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization header-
        for a Basic Authentication:
            Return None if authorization_header is None
            Return None if authorization_header is not a string
            Return None if authorization_header doesn’t start by Basic-
            (with a space at the end)
            Otherwise, return the value after Basic (after the space)
            You can assume authorization_header contains only one Basic
        """

        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header[0:6] == "Basic ":
            return authorization_header[6:]

#!/usr/bin/env python3
"""class session"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """inherits Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id:
        Return None if user_id is None
        Return None if user_id is not a string
        Otherwise:
        - Generate a session ID usiing uuid$() like id in Base
        - use theID as key dictioney for user_id_by_session_id,
            the value must be user_id
        - Return session ID
        The same user_id can have multiple Session ID - indeed,
        the user_id is the value in the dictionary user_id_by_session_id
        """
        if user_id is None:
            return None
        elif type(user_id) != str:
            return None
        else:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

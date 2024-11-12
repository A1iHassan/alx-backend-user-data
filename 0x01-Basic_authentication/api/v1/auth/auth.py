#!/usr/bin/env python3
"""Module for class Auth"""

from flask import request
from typing import List, TypeVar, Optional
import fnmatch


class Auth:
    """Auth class for handling authorization"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if auth is required.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True


    def authorization_header(self, request=None) -> Optional[str]:
        """Returns None for authorization header"""
        return None

    def current_user(self, request=None) -> Optional[TypeVar('User')]:
        """Returns None for the current user"""
        return None

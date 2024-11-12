#!/usr/bin/env python3
"""Module for class Auth"""

from flask import request
from typing import List, TypeVar, Optional


class Auth:
    """Auth class for handling authorization"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False as authentication is not required"""
        return False

    def authorization_header(self, request=None) -> Optional[str]:
        """Returns None for authorization header"""
        return None

    def current_user(self, request=None) -> Optional[TypeVar('User')]:
        """Returns None for the current user"""
        return None

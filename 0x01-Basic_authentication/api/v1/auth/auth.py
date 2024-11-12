#!/usr/bin/env python3
"""Module for class Auth"""
import request from flask


class Auth():
    """
    class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False"""
        return False


    def authorization_header(self, request=None) -> str:
        """returns None"""
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """returns None"""
        return None

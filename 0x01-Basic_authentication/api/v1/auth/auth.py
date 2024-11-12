#!/usr/bin/env python3
"""
Module for authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Template for all authentication system implementations."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for a given path.

        Returns True if `path` is None, `excluded_paths` is None or empty,
        or if `path` is not in `excluded_paths`.
        `excluded_paths` contains string paths always ending with a slash,
        and this method is slash-tolerant, e.g., `/api/v1/status` and
        `/api/v1/status/` are equivalent.

        Args:
            path (str): The path to check against the list of excluded paths.
            excluded_paths (List[str]): The list of paths to exclude.

        Returns:
            bool: True if the path requires authentication, False otherwise.
        """
        if not path:
            return True
        if not excluded_paths:
            return True

        path = path.rstrip("/")

        for excluded_path in excluded_paths:
            if excluded_path.endswith("*") and \
                    path.startswith(excluded_path[:-1]):
                return False
            elif path == excluded_path.rstrip("/"):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the value of the Authorization header from the request.

        Args:
            request (Request, optional): Flask request object. Defaults to None.

        Returns:
            str: The value of the Authorization header or None if not present.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user based on the request.

        This method currently returns None and will be implemented later.

        Args:
            request (Request, optional): Flask request object. Defaults to None.

        Returns:
            TypeVar('User'): Currently returns None; type `User` to be defined.
        """
        return None

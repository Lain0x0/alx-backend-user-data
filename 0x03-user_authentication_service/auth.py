#!/usr/bin/env python3
""" Hashing Passwords Using bcrypt"""
import bcrypt
from db import DB


def _hash_password(password: str) -> str:
    """bcrypt for pass hashing"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """User Registration"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

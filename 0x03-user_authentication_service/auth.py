#!/usr/bin/env python3
"""bla bla
"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4

from typing import Union


def _hash_password(password: str) -> str:
    """_hashed_password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """_generate_uuid
    """
    id = uuid4()
    return str(id)


class Auth:
    """Auth class
    """

    def __init__(self):
        """_init_
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> Union[None, User]:
        """register_user
        """
        try:

            self._db.find_user_by(email=email)
        except NoResultFound:

            return self._db.add_user(email, _hash_password(password))

        else:

            raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """valid_login
        """
        try:

            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """create_session
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            user.session_id = _generate_uuid()
            return user.session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """get_user_from_session_id
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        else:
            return user

    def destroy_session(self, user_id: str) -> None:
        """destroy_session
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None
        else:
            user.session_id = None
            return None

    def get_reset_password_token(self, email: str) -> str:
        """get_reset_password_token
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        else:
            user.reset_token = _generate_uuid()
            return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """update_password
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        else:
            user.hashed_password = _hash_password(password)
            user.reset_token = None
            return None

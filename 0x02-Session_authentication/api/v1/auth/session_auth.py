#!/usr/bin/env python3
"""User Basic 
authentication
Session
"""

from uuid import uuid4
from flask import request
from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Session authentication class"""
    user_id_by_session_id = {}

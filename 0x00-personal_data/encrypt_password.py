#!/usr/bin/env python3
"""
Securing password by hashing
using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Using bcrypt for password hashing """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

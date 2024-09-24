#!/usr/bin/env python3
""" Hashing Passwords Using bcrypt"""
import bcrypt


def _hash_password(password: str) -> str:
    """bcrypt for pass hashing"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

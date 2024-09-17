#!/usr/bin/env python3
""" Using index.py to check files syntax and logic """
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route("/unauthorized", methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ GET /api/v1/unauthorized """
    abort(401)

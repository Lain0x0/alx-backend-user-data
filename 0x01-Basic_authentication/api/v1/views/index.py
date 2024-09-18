#!/usr/bin/env python3
"""1. Error handler: Unauthorized
   2. Error handler: Forbidden
"""
from flask import jsonify, abort


@app_views.route('/unauthorized/', strict_slashes=False)
def unauthorized() -> None:
    """GET /api/v1/unauthorized"""
    abort(401)

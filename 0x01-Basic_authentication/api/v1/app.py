#!/usr/bin/env python3
"""1. Error handler: Unauthorized
   2. Error handler: Forbidden
"""
import os
from flask import Flask, jsonify, abort
from flask_cors import CORS, cross_origin
from api.v1.views import app_views


app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app_views.route('/unauthorized/', strict_slashes=False)
def unauthorized() -> None:
    """GET /api/v1/unauthorized
    Return:
      - Unauthorized error.
    """
    abort(401)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)

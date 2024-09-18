#!/usr/bin/env python3
"""1. Error handler: Unauthorized
   2. Error handler: Forbidden
"""
import os
from flask import Flask, jsonify, abort
from flask_cors import CORS, cross_origin
from api.v1.views import app_views
from api.v1.auth.auth import Auth


app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


auth = None
if os.getenv("AUTH_TYPE") == "basic_auth":
    auth = BasicAuth()
elif os.getenv("AUTH_TYPE") == "auth":
    auth = Auth()


@app.before_request
def before_request_func():
    """bla bla bla annoted"""
    if auth is None:
        return
    if not auth.require_auth(request.path, ['/api/v1/status/',
                                            '/api/v1/unauthorized/',
                                            '/api/v1/forbidden/']):
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)


@app_views.route('/unauthorized/', strict_slashes=False)
def unauthorized() -> None:
    """GET /api/v1/unauthorized
    Return:
      - Unauthorized error.
    """
    abort(401)


@app.errorhandler(401)
def unauthorized_error(error) -> tuple:
    """Return a JSON response for 401 Unauthorized error."""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden handler."""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)

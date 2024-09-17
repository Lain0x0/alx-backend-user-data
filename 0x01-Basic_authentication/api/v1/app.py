#!/usr/bin/env python3
""" Auth User using flask and some encoders

for data user """
from os import getenv
from flask import Flask, jsonify, abort
from flask_cors import (CORS, cross_origin)
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(401)
def err_handl(error) -> str:
    """Intialize """
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)

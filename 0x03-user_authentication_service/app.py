#!/usr/bin/env python3
""" Set up Flask for web Dev and configure it """
from flask import Flask, abort, jsonify, redirect, request, url_for
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /users"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

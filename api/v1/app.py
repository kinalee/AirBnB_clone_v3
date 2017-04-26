#!/usr/bin/python3
"""

"""
from api.v1.views import app_views
from flask import Blueprint, Flask, jsonify
from flask_cors import CORS
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, origins="0.0.0.0")


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    return(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    apiHost = '0.0.0.0'
    apiPort = '5000'
    if os.getenv('HBNB_API_HOST'):
        apiHost = os.getenv('HBNB_API_HOST')
    if os.getenv('HBNB_API_PORT'):
        apiPort = os.getenv('HBNB_API_PORT')
    app.run(host=apiHost, port=apiPort)

#!/usr/bin/python3
"""

"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    return(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    if os.getenv('HBNB_API_HOST'):
        host = 'HBNB_API_HOST'
    if os.getenv('HBNB_API_PORT'):
        port = 'HBNB_API_PORT'
    app.run(host='0.0.0.0', port='5000')

#!/usr/bin/python3
"""

"""
from flask import Flask
import json



app = Flask(__name__)
from models import storage
from api.v1.views import app_views


app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    page = json.dumps({"error": "Not found"}, indent=2)
    return (page + "\n")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

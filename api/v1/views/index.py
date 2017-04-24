#!/usr/bin/python3
"""
Index for app_views
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


models = ["User", "Amenity", "City", "Place", "Review", "State"]


@app_views.route('/status')
def status():
    return(jsonify({"status": "OK"}))


@app_views.route('/stats')
def stats():
    statsDict = {}
    for model in models:
        for stats in storage.count(model):
            statsDict[model] = stats
    return(jsonify(sorted(statsDict)))

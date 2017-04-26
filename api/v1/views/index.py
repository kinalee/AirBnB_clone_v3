#!/usr/bin/python3
"""
Index for app_views
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


models = {"amenities": "Amenity",
          "cities": "City",
          "places": "Place",
          "reviews": "Review",
          "states": "State",
          "users": "User"}


@app_views.route('/status')
def status():
    return(jsonify({"status": "OK"}))


@app_views.route('/stats')
def stats():
    statsDict = {}
    for k, v in models.items():
        statsDict[k] = storage.count(v)
    print(statsDict)
    return(jsonify(statsDict))

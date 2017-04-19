#!/usr/bin/python3
"""
"""
from api.v1.views import app_views
from models import storage
import json

models = ["User", "Amenity", "City", "Place", "Review", "State"]

@app_views.route('/status')
def status():
    status = json.dumps({"status": "OK"}, indent=2)
    return(status + "\n")

@app_views.route('/stats')
def stats():
    statsDict = {}
    for model in models:
        for stats in storage.count(model):
            statsDict[model] = stats
    return(json.dumps(statsDict, indent=2, sort_keys=True))

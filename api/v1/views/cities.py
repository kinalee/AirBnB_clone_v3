#!/usr/bin/python3
"""
handles all default RestFul API actions for City object
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import City, storage, BaseModel

"""
@app_views.route('/states/<state_id>/cities')


@app_views.route('/states/<state_id/')
"""

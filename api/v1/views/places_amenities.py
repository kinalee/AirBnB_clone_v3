#!/usr/bin/python3
"""
handles all default RestFul API actions between Place objects Amenity Objects
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import *
import os

#!/usr/bin/python3
"""
init module for views package
"""
from flask import Blueprint


app_views = Blueprint('views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.user import *
from api.v1.views.places import *
from api.v1.views.places_amenities import *
from api.v1.views.places_reviews import *

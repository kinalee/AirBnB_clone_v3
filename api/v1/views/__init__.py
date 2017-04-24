#!/usr/bin/python3
"""
init module for views package
"""
from api.v1.views.index import *
from api.v1.views.states import *
from flask import Blueprint


app_views = Blueprint('views', __name__, url_prefix='/api/v1')

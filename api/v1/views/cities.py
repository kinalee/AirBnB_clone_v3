#!/usr/bin/python3
"""
handles all default RestFul API actions for City object
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import *


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def getStateCity(state_id):
    """ Retrieves list of given City object of a State """
    if storage.get("State", state_id) is None:
        abort(404)
    try:
        cities = storage.all("City")
        cityList = []
        for city in cities.values():
            for k, v in city.to_json().items():
                if (k == "state_id" and v == state_id):
                    cityList.append(city.to_json())
        return (jsonify(cityList))
    except:
        abort(404)


@app_views.route('/cities/<city_id>',
                 methods=['GET'], strict_slashes=False)
def getCity(city_id):
    """ Retrieves list of given City object """
    try:
        city = storage.get("City", city_id)
        return (jsonify(city.to_json()))
    except:
        abort(404)


@app_views.route('/cities/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def deleteCity(city_id):
    """ Deletes a City object """
    try:
        city = storage.get("City", city_id)
        if city is None:
            abort(404)
        storage.delete(city)
        storage.save()
        return (jsonify({}), 200)
    except:
        abort(404)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def createCity(state_id):
    """ Creates a City object """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if "name" not in data:
        abort(400, 'Missing name')
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    data['state_id'] = state_id
    city = City(data)
    storage.new(city)
    storage.save()
    return(jsonify(storage.get("City", city.id).to_json()), 201)


@app_views.route('/cities/<city_id>',
                 methods=['PUT'], strict_slashes=False)
def updateCity(city_id):
    """ Updates a City object """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    for k, v in data.items():
        if (k != "id" and k != "created_at" and k != "updated_at"):
            setattr(city, k, v)
    city.save()
    city_json = city.to_json()
    return(jsonify(city_json), 200)

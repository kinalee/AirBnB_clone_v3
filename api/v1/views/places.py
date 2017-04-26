#!/usr/bin/python3
"""
handles all default RestFul API actions for Place object
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import *


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def getCityPlace(city_id):
    """ Retrieves list of given Place object of a City """
    places = storage.all("City")
    if storage.get("City", city_id) is None:
        abort(404)
    placeList = []
    for place in places.values():
        for k, v in place.to_json().items():
            if (k == "city_id" and v == city_id):
                placeList.append(place.to_json())
    return (jsonify(placeList))


@app_views.route('/places/<place_id>',
                 methods=['GET'], strict_slashes=False)
def getPlace(city_id):
    """ Retrieves list of given Place object """
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    return (jsonify(place.to_json()))


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def deletePlace(place_id):
    """ Deletes a Place object """
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    storage.delete(palace)
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def createPlace(city_id):
    """ Creates a Place object """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if "user_id" not in data:
        abort(400, 'Missing user_id')
    if "name" not in data:
        abort(400, 'Missing name')
    if storage.get("User", data['user_id']) is None:
        abort(404)
    data['city_id'] = city_id
    newPlace = Place(data)
    storage.new(newPlace)
    storage.save()
    return(jsonify(storage.get("Place", newPlace.id).to_json()), 201)


@app_views.route('/places/<place_id>',
                 methods=['PUT'], strict_slashes=False)
def updatePlace(place_id):
    """ Updates a Place object """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    for k, v in data.items():
        if(k != "id" and k != "user_id" and
           k != "city_id" and k != "created_at" and k != "updated_at"):
            setattr(place, k, v)
    place.save()
    place_json = place.to_json()
    return(jsonify(place_json), 200)

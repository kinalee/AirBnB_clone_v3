#!/usr/bin/python3
"""
handles all default RestFul API actions for Amenity object
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import *


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def getAmenities(amenity_id=None):
    """ Retrieves list of all or given State object """
    if amenity_id is None:
        amenities = storage.all("Amenity")
        amenityList = []
        for amenity in amenities.values():
            amenityDict = {}
            for k, v in amenity.to_json().items():
                amenityDict[k] = v
            amenityList.append(amenityDict)
        return (jsonify(amenityDict))
    else:
        try:
            amenity = storage.get("Amenity", amenity_id)
            return (jsonify(amenity.to_json()))
        except:
            abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteAmenity(amenity_id):
    """ Deletes an Amenity object """
    try:
        amenity = storage.get("Amenity", state_id)
        storage.delete(amenity)
        storage.save()
        return (jsonify({}), 200)
    except:
        abort(404)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def createAmenity():
    """ Creates an Amenity object """
    try:
        data = request.get_json()
    except:
        abort(400, 'Not a JSON')
    if "name" not in data:
        abort(400, 'Missing name')
    newAmenity = Amenity(data)
    storage.new(newAmenity)
    storage.save()
    return (jsonify(storage.get("Amenity", newAmenity.id).to_json()), 201)


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def updateAmenity(amenity_id):
    """ Updates an Amenity object """
    try:
        data = request.get_json()
    except:
        abort(400, 'Not a JSON')
    try:
        amenity = storage.get("Amenity", amenity_id)
        for k, v in data.items():
            if k != "id" and k != "created_at" and k != "updated_at":
                setattr(amenity, k, v)
        amenity.save()
        amenity_json = amenity.to_json()
        return(jsonify(amenity_json), 200)
    except:
        abort(404)

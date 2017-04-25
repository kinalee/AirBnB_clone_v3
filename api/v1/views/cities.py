#!/usr/bin/python3
"""
handles all default RestFul API actions for City object
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import BaseModel, City, storage


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def getStateCity(state_id):
    """ Retrieves list of given City object of a State """
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


@app_views.route('/api/v1/cities/<city_id>', methods=['GET'])
def getCity(city_id):
    """ Retrieves list of given City object """
    try:
        city = storage.get("City", city_id)
        return (jsonify(city.to_json()))
    except:
        abort(404)



@app_views.route('/api/v1/cities/<city_id>', methods=['DELETE'])
def deleteCity(city_id):
    """ Deletes a City object """
    try:
        city = storage.get("City", city_id)
        storage.delete(city)
        storage.save()
        return (jsonify({}), 200)
    except:
        abort(404)


@app_views.route('/api/v1/states/<state_id>/cities', methods=['POST'])
def createCity(state_id):
    """ Creates a City object """
    try:
        data = request.get_json()
    except:
        abort(400, 'Not a JSON')
    if "name" not in data:
        abort(400, 'Missing name')
    print("what is going on?")
    newCity = City(data)
    print(newCity)
    storage.new(newCity)
    storage.save()
    return(jsonify(storage.get("City", newCity.id).to_json()), 201)


@app_views.route('/api/v1/cities/<city_id>', methods=['PUT'])
def updateCity(city_id):
    """ Updates a City object """
    try:
        data = request.get_json()
    except:
        abort(400, 'Not a JSON')
    try:
        city = storage.get("City", city_id)
        for k, v in data.items():
            if (k != "id" and k != "created_at" and k != "updated_at"):
                city.__dict__[k] = v
        city.save()
        return(jsonify(city.to_json()), 200)
    except:
        abort(400)

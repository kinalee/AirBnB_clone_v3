#!/usr/bin/python3
"""
handles all default RestFul API actions for User object
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import *


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def getUser(user_id=None):
    """ Retrieves list of all or given User object """
    if user_id is None:
        users = storage.all("User")
        userList = []
        for user in users.values():
            userDict = {}
            for k, v in user.to_json().items():
                userDict[k] = v
            userList.append(userDict)
        return (jsonify(userList))
    else:
        user = storage.get("User", user_id)
        if user is None:
            abort(404)
        user_json = user.to_json()
        return (jsonify(user_json))


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteUser(user_id):
    """ Deletes a State object """
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def createUser():
    """ Creates a User object """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if "email" not in data:
        abort(400, 'Missing email')
    if "password" not in data:
        abort(400, password)
    newUser = User(data)
    storage.new(newUser)
    storage.save()


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def updateUser(user_id):
    """ Updates a User object """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    for k, v in data.items():
        if k != "id" and k != "created_at" and k != "updated_at":
            setattr(user, k, v)
    user.save()
    user_json = user.to_json()
    return(jsonify(user_json), 200)

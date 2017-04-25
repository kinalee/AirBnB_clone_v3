#!/usr/bin/python3
"""
handles all default RestFul API actions for State object
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import BaseModel, State, storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def getState(state_id=None):
    """ Retrieves list of all or given State object """
    if state_id is None:
        states = storage.all("State")
        stateList = []
        for state in states.values():
            stateDict = {}
            for k, v in state.to_json().items():
                stateDict[k] = v
            stateList.append(stateDict)
        return (jsonify(stateList))
    else:
        state = storage.get("State", state_id)
        if state is None:
            abort(404)
        state_json = state.to_json()
        return (jsonify(state_json))


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteState(state_id):
    """ Deletes a State object """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def createState():
    """ Creates a State object """
    data = request.get_json()
    if date in None:
        abort(400, 'Not a JSON')
    if "name" not in data:
        abort(400, 'Missing name')
    newState = State(data)
    storage.new(newState)
    storage.save()
    state_json = storage.get("State", newState.id).to_json()
    return (jsonify(state_json), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def updateState(state_id):
    """ Updates a State object """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    for k, v in data.items():
        if k != "id" and k != "created_at" and k != "updated_at":
            setattr(state, k, v)
    state.save()
    state_json = state.to_json()
    return(jsonify(state_json), 200)

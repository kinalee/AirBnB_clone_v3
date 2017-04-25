#!/usr/bin/python3
"""
handles all default RestFul API actions for State object
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import State, storage, BaseModel


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
        try:
            state = storage.get("State", state_id)
            return (jsonify(state.to_json()))
        except:
            abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteState(state_id):
    """ Deletes a State object """
    try:
        state = storage.get("State", state_id)
        storage.delete(state)
        storage.save()
        return (jsonify({}), 200)
    except:
        abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def createState():
    """ Creates a State object """
    try:
        data = request.get_json()
    except:
        abort(400, 'Not a JSON')
    if "name" not in data:
        abort(400, 'Missing name')
    newState = State(data)
    storage.new(newState)
    storage.save()
    return (jsonify(storage.get("State", newState.id).to_json()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def updateState(state_id):
    """ Updates a State object """
    try:
        data = request.get_json()
    except:
        abort(400, 'Not a JSON')
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    for k, v in data.items():
        if k != "id" and k != "created_at" and k != "updated_at":
            state.__dict__[k] = v
    state.save()
    state_json = state.to_json()
    return(jsonify(state_json), 200)

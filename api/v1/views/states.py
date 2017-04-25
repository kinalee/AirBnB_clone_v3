#!/usr/bin/python3
"""
handles all default RestFul API actions for State object
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import State, storage, BaseModel


@app_views.route('/states/', methods=['GET'])
@app_views.route('/states/<state_id>', methods=['GET'])
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


@app_views.route('/states/<state_id>', methods=['DELETE'])
def deleteState(state_id):
    """ Deletes a State object """
    try:
        state = storage.get("State", state_id)
        storage.delete(state)
        storage.save()
        return (jsonify({}), 200)
    except:
        abort(404)


@app_views.route('/states/', methods=['POST'])
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


@app_views.route('/states/<state_id>', methods=['PUT'])
def updateState(state_id):
    """ Updates a State object  """
    try:
        data = request.get_json()
    except:
        abort(400, 'Not a JSON')
    try:
        state = storage.get("State", state_id)
        for k, v in data.items():
            if k != "id" and k != "created_at" and k != "updated_at":
                state.__dict__[k] = v
        state.save()
        return(jsonify(state.to_json()), 200)
    except:
        abort(404)

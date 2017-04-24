#!/usr/bin/python3
"""
handles all default RestFul API actions for State object
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import State, storage, BaseModel


@app_views.route('/states/', methods=['GET'])
@app_views.route('/states/<stateId>', methods=['GET'])
def getState(stateId=None):
    """ Retrieves list of all or given State object """
    if stateId is None:
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
            state = storage.get("State", stateId)
            return (jsonify(state.to_json()))
        except:
            abort(404)


@app_views.route('/states/<stateId>', methods=['DELETE'])
def deleteState(stateId):
    """ Deletes a State object """
    try:
        state = storage.get("State", stateId)
        storage.delete(state)
        storage.save()
        return (jsonify({}), 200)
    except:
        abort(404)


@app_views.route('/states/', methods=['POST'])
def createState():
    """ Creates a State object """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if "name" not in data:
        abort(400, 'Missing name')
    newState = State(data)
    storage.new(newState)
    storage.save()
    return (jsonify(storage.get("State", newState.id).to_json()), 201)


@app_views.route('/states/<stateId>', methods=['PUT'])
def updateState(stateId):
    """ Updates a State object  """
    try:
        data = request.get_json()
    except:
        abort(400, 'Not a JSON')
    try:
        state = storage.get("State", stateId).to_json()
        for k, v in data.items():
            if (k != "id" and k != "created_at" and k != "updated_at"):
                state[k] = v
        storage.save()
        return(jsonify(state), 200)
    except:
        abort(404)

#!/usr/bin/python3
"""
handles all default RestFul API actions for State object
"""
from api.v1.views import app_views
from flask import abort, jsonify
from models import State, storage, BaseModel


@app_views.route('/states/', methods=['GET'])
@app_views.route('/states/<state_id>', methods=['GET'])
def stateList(state_id=None):
    states = storage.all("State")
    if state_id is None:
        stateList = []
        for state in states.values():
            stateDict = {}
            for k, v in state.to_json().items():
                stateDict[k] = v
            stateList.append(stateDict)
        return (jsonify(stateList))
    else:
        stateDict = {}
        for s_id, data in states.items():
            if s_id == state_id:
                for k, v in data.to_json().items():
                    stateDict[k] = v
                    return (jsonify(stateDict))
        abort(404)

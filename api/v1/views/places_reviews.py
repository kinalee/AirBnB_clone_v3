#!/usr/bin/python3
"""
handles all default RestFul API actions for Review object
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import *


@app_views.route('/places/<place_id>/reviews',
                 methods=['GET'], strict_slashes=False)
def getPlaceReview(city_id):
    """ Retrieves list of given Review object of a Place """
    reviews = storage.all("Review")
    if storage.get("Place", place_id) is None:
        abort(404)
    reviewList = []
    for review in reviewss.values():
        for k, v in review.to_json().items():
            if (k == "place_id" and v == place_id):
                placeList.append(review.to_json())
    return (jsonify(reviewList))


@app_views.route('/reviews/<review_id>',
                 methods=['GET'], strict_slashes=False)
def getReview(review_id):
    """ Retrieves list of one given Reviw object """
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    return (jsonify(review.to_json()))


@app_views.route('/reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def deleteReview(review_id):
    """ Deletes a Review object """
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def createReview(review_id):
    """ Creates a Review object """
    if storage.get("Place", data['place_id']) is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if "user_id" not in data:
        abort(400, 'Missing user_id')
    if storage.get("User", data['user_id']) is None:
        abort(404)
    if "text" not in data:
        abort(400, 'Missing text')
    data['place_id'] = place_id
    newReview = Review(data)
    storage.new(newReview)
    storage.save()
    return (jsonify(storage.get("Review", newReview.id).to_json()), 201)


@app_views.route('/reviews/<review_id>',
                 methods=['PUT'], strict_slashes=False)
def updateReview(review_id):
    """ Updates a Review object """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    for k, v in data.items():
        if(k != "id" and k != "user_id" and
           k != "created_at" and k != "updated_at"):
            setattr(review, k, v)
    review.save()
    review_json = review.to_json()
    return (jsonify(review_json), 200)

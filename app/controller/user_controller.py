from flask import Blueprint, request, jsonify
from app.data.store import store

user_bp = Blueprint(
    "user", 
    __name__, 
    url_prefix="/api/v1/users/")


@user_bp.route("", methods=["GET"])
def list_user():
    return jsonify(store["users"]), 200

@user_bp.route("", methods=["POST"])
def create_user():
    return {
        "variable" : "this is what was returned"
    }, 201


@user_bp.route("/<id>", methods=["GET"])
def get_one_user(id):
    return {
        "message": "not implemented yet"
    }

@user_bp.route("/<id>", methods=["PUT", "PATCH"])
def update_user(id):
    pass


@user_bp.route("/<id>", methods=["DELETE"])
def delete_user(id):
    pass

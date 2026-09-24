from flask import Blueprint, request, jsonify
from app.data.store import store

dept_bp = Blueprint(
    "dept", 
    __name__, 
    url_prefix="/api/v1/dept/")


@dept_bp.route("", methods=["GET"])
def list_dept():
    return jsonify(store["depts"]), 200

@dept_bp.route("", methods=["POST"])
def create_dept():
    return {
        "variable" : "this is what was returned"
    }, 201


@dept_bp.route("/<id>", methods=["GET"])
def get_one_dept(id):
    return {
        "message": "not implemented yet"
    }

@dept_bp.route("/<id>", methods=["PUT", "PATCH"])
def update_dept(id):
    pass


@dept_bp.route("/<id>", methods=["DELETE"])
def delete_dept(id):
    pass

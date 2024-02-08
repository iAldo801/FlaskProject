from flask import Blueprint, request, jsonify

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/api/user", methods=["GET"])
def get_user():
    if request.method == "GET":
        return jsonify({ "message": "Hello, World!"})
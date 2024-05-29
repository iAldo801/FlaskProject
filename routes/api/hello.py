from flask import Blueprint, request, jsonify

hello_blueprint = Blueprint("hello", __name__)

@hello_blueprint.route("/api/hello", methods=["GET"])
def get_user():
    if request.method == "GET":
        return jsonify({ "message": "Hello, World!"})
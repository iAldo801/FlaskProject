from flask import Blueprint, request, jsonify
from utils.db import get_user_info  # Import the get_user_info function

user_info_blueprint = Blueprint("user_info", __name__)

@user_info_blueprint.route("/api/info", methods=["GET"])
def get_user_info_route():
    username = request.cookies.get('username')
    if not username:
        return jsonify({"error": "Not logged in"}), 401

    user = get_user_info(username)  # Call the get_user_info function with the username
    if not user:
        return jsonify({"error": "User not found"}), 404
    else:
        user_info = {
            "id": user[0],
            "username": user[1],
            "created_at": user[3],
            "last_login": user[4]
        }
        return jsonify(user_info)

from flask import Blueprint
from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from werkzeug.security import generate_password_hash
from models import User

bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route('/register', methods=('POST',))
def register():
  data = request.get_json()
  password = data['password']
  username = data['username']

  user = User.User.get_by_username(username)
  if user is None:
    user = User(
      username=username,
      password=generate_password_hash(password)
    )

    User.User.add()
    access_token = create_access_token(identity=user.user_id)
    refresh_token = create_refresh_token(identity=user.user_id)

    response = jsonify()
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response, 201
  else:
    return jsonify(message="Unable to create user."), 400
@bp.route('/login', methods=('POST',))
def login():
  data = request.get_json()
  username = data['username']
  password = data['password']
  user = User.User.authenticate(username, password)
  if user:
    access_token = create_access_token(identity=user.user_id)
    refresh_token = create_refresh_token(identity=user.user_id)

    response = jsonify()
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)
    return response, 201
  else:
    return jsonify(message="Unauthorized"), 401
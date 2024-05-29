from flask import Blueprint, make_response, redirect, url_for

logout_blueprint = Blueprint("logout", __name__)

@logout_blueprint.route("/auth/logout")
def logoutRoute():
    resp = make_response(redirect(url_for('login.loginRoute')))
    resp.set_cookie('username', '', expires=0)
    return resp
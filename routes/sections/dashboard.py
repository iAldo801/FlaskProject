from flask import Blueprint, render_template, redirect, render_template, request, url_for

dashboard_blueprint = Blueprint("dashboard", __name__)

@dashboard_blueprint.route("/dashboard")
def dashboardRoute():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login.loginRoute'))

    return render_template('dashboard.html', username=username)
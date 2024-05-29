from flask import Blueprint, render_template, redirect, make_response, request, url_for
from utils.db import get_db_connection
from werkzeug.security import check_password_hash
import psycopg2

login_blueprint = Blueprint("login", __name__)
conn = get_db_connection()

@login_blueprint.route("/auth/login", methods=["GET", "POST"])
def loginRoute():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()

        if user and check_password_hash(user[2], password):
            # Update last_login for the user
            cur.execute("""
                UPDATE users
                SET last_login = TO_CHAR(NOW(), 'Day, DD Month YYYY HH12:MI:SS AM')
                WHERE id = %s
            """, (user[0],))
            conn.commit()
            cur.close()
            conn.close()

            resp = make_response(redirect(url_for('dashboard.dashboardRoute')))
            resp.set_cookie('username', username)
            return resp
        else:
            cur.close()
            conn.close()
            return 'Invalid credentials'

    return render_template("login.html")

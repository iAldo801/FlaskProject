from flask import Blueprint, render_template, redirect, render_template, request, url_for
from utils.db import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

register_blueprint = Blueprint("register", __name__)
conn = get_db_connection()

@register_blueprint.route("/auth/register", methods=["GET", "POST"])
def registerRoute():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('login.loginRoute'))

    return render_template("register.html")
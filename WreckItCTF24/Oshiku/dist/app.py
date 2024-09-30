from flask import *
import sqlite3
import os
import subprocess

app = Flask(__name__)
app.secret_key = 'os.urandom(8)'

# Database connection
DATABASE = "database.db"
def query_database(name):
    query = 'sqlite3 database.db "SELECT biography FROM oshi WHERE name=\'' + str(name) +'\'\"'
    result = subprocess.check_output(query, shell=True, text=True)
    return result

@app.route("/")
def index():
    role = session.get('role')
    if role == "admin":
        return redirect(url_for('admin'))
    elif role == "guest":
        return redirect(url_for('guest'))
    else:
        return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "guest" and password == "guest":
            session['username'] = username
            session['role'] = "guest"
            return redirect(url_for('guest'))
        else:
            return jsonify({"msg": "Bad username or password"}), 401
    return render_template("login.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if 'role' not in session or session['role'] != "admin":
        return jsonify({"msg": "Access forbidden: Admins only"}), 403

    if request.method == "POST":
        selected_name = request.form.get("oshi_name")
        biography = query_database(selected_name)
        return render_template("admin.html", biography=biography)
    return render_template("admin.html", biography="")

@app.route("/guest", methods=["GET", "POST"])
def guest():
    if 'role' not in session or session['role'] != "guest":
        return jsonify({"msg": "Access forbidden: Guests only"}), 403
    return render_template("guest.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
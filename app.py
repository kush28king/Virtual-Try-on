from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Dummy database for user authentication
database = {'nachi': '123', 'james': 'aas', 'kushagra': '2345'}

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username not in database:
        return render_template("login.html", info="User not found")

    if database[username] != password:
        return render_template("login.html", info="Invalid credentials")

    return redirect(url_for("virtual_dressing"))
import subprocess
@app.route("/virtual_dressing")
def virtual_dressing():
    subprocess.Popen(["python", "FinalMiniProject.py"])   # This runs the ML model
    return "Virtual Dressing System Launched!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)

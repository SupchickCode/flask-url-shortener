from flask import render_template, url_for, flash, redirect
from project import app
# from project.forms import RegistrationForm, LoginForm
# from project.models import User, Post

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
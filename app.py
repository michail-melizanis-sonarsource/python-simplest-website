import sys
import os  # For environment variables and file handling

from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash  # Flask components
from flask_sqlalchemy import SQLAlchemy  # For database integration
from flask_migrate import Migrate  # For database migrations
from flask_wtf import FlaskForm  # For creating forms
from wtforms import StringField, SubmitField  # Form fields
from wtforms.validators import DataRequired  # Form validation
from flask_bootstrap import Bootstrap  # For Bootstrap integration
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required  # For user authentication

# Flask app initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database configuration

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model for authentication
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Example form using Flask-WTF
class NameForm(FlaskForm):
    name = StringField('Enter your name:', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/", methods=["GET", "POST"])
def home():
    form = NameForm()
    if form.validate_on_submit():
        flash(f"Hello, {form.name.data}!", "success")
        return redirect(url_for('home'))
    return render_template("home.html", form=form)

@app.route("/account", methods=["POST", "GET"])
def account():
    usr = "<User Not Defined>"
    if request.method == "POST":
        usr = request.form["name"]
        if not usr:
            usr = "<User Not Defined>"
    return render_template("account.html", username=usr)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials. Please try again.", "danger")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))

@app.route("/about")
@app.route("/about/<name>")
def about_name(name=None):
    return render_template("about.html", username=name)

@app.route("/about/<name>/<int:age>")
def about_name_age(name, age):
    return render_template("about.html", username=name, age=age)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/<name>")
def contact_name(name):
    return render_template("contact.html", username=name)

@app.route("/contact/<name>/<int:age>")
def contact_name_age(name, age):
    return render_template("contact.html", username=name, age=age)

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/services/<name>")
def services_name(name):
    return render_template("services.html", username=name)

@app.route("/services/<name>/<int:age>")
def services_name_age(name, age):
    return render_template("services.html", username=name, age=age)

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == "__main__":
    app.run(debug=True, port=4949)

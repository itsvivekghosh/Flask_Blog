from flask import Flask, render_template, url_for, redirect, flash, request
from flaskblog import app
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        "author": "Vivek Ghosh",
        "title": "Blog Post 1",
        "content": "Content 1",
        "date_posted": "May 20th, 2020",
    },
    {
        "author": "Vivek Kumar Ghosh",
        "title": "Blog Post 2",
        "content": "Content 2",
        "date_posted": "May 22th, 2020",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Custom Title", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About Us")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_pass
        )
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created for! You can Sign In Now", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Sign Up", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Invalid Username or Password!", "danger")
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")

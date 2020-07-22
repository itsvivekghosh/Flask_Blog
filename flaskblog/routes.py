from flask import Flask, render_template, url_for, redirect, flash
from flaskblog import app
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm



posts = [
    {
        'author': "Vivek Ghosh",
        "title": "Blog Post 1",
        'content': "Content 1",
        "date_posted": "May 20th, 2020"
    },
    {
        'author': "Vivek Kumar Ghosh",
        "title": "Blog Post 2",
        'content': "Content 2",
        "date_posted": "May 21th, 2020"
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Custom Title", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About Us")


@app.route("/register", methods=['GET', "POST"])
def register():
	form = RegistrationForm()

	if form.validate_on_submit():
		flash("Account created for {}!".format(form.username.data), 'success')
		return redirect(url_for("home"))

	return render_template("register.html", title="Sign Up", form=form)


@app.route("/login", methods=['POST', "GET"])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		if form.email.data == 'soapmactevis1@gmail.com' and form.password.data == 'Vivek@1999':
			return redirect(url_for("home"))
		else:
			flash("Invalid Username or Password!", 'danger')	
	return render_template("login.html", title="Sign In", form=form)

from flask import Blueprint, render_template, request, flash, url_for, redirect

APP = Blueprint ('APP', __name__)

@APP.route('/')
def index():
    return redirect(url_for('APP.home'))

@APP.route('/home')
def index():
    return render_template('index.html')

@APP.route('/new')
def index():
    return render_template('new.html')
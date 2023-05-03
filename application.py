from flask import Flask

application = Flask(__name__)

@application.route('/')
def welcome_page():
    return "Welcome to Lab"


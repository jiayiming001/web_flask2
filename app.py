from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import Blueprint
from routes.todo import main as todo_routes

app = Flask(__name__)

app.secret_key = "jia yi ming"

app.register_blueprint(todo_routes, url_perfix='/todo')

if __name__ == '__main__':
    config = dict(
        debug = True,
        host = "0.0.0.0",
        port = 2000,
    )
    app.run(**config)

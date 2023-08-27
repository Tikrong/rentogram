import flask
from flask import request

from rentogram import app, logger
from rentogram.models import Appartment


@app.route("/")
def main():
    """Страница удаления зависшего чека."""

    collection = {"hello": 1, "world": 2, "!": [1, 2, 3, 4, 5]}

    return flask.jsonify(collection)


@app.route("/get_apartments")
def get_appartments():
    """Эндпоинт, который возвращает весь список игр"""

    appartments = Appartment.get_apartments()

    return flask.jsonify(appartments)

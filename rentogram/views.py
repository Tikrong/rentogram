import flask
from flask_headers import headers
from flask import request

from rentogram import app, logger
from rentogram.models import Apartment
from rentogram.utils import parse_and_add_apartments


@app.route("/")
def main():
    """Страница удаления зависшего чека."""

    collection = {"hello": 1, "world": 2, "!": [1, 2, 3, 4, 5]}

    return flask.jsonify(collection)


@app.route("/get_apartments")
@headers({'Access-Control-Allow-Origin': '*'})
def get_appartments():
    """Эндпоинт, который возвращает весь список игр"""

    appartments = Apartment.get_apartments()

    return flask.jsonify(appartments)


@app.route("/add_apartments", methods=['POST'])
def add_apartaments():
    if payload := request.json:
        if payload['api_key'] and payload['api_key'] == app.config.get('ADD_APARTMENTS_API_KEY'):
            if apartments := payload['apartments']:
                added_counter = parse_and_add_apartments(apartments)
                return f'{added_counter} apartments were added', 200

    return "Error, couldn't add apartments", 400


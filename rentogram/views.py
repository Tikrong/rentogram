import flask
from flask import request
import json

from rentogram import app, logger
from rentogram.models import Apartment
from rentogram.utils import parse_and_add_apartments


@app.route("/")
def main():
    """Страница удаления зависшего чека."""

    collection = {"hello": 1, "world": 2, "!": [1, 2, 3, 4, 5]}

    return flask.jsonify(collection)


@app.route("/get_apartments")
def get_appartments():
    """Эндпоинт, который возвращает весь список игр"""

    appartments = Apartment.get_apartments()

    return flask.jsonify(appartments)


@app.route("/add_apartments")
def add_apartaments():

    # raw_data = {"snyat_kvartiruw": {4199: """#Сдам в Батуми
    #             На долгий срок от 1 года. Новая 2 комнатная  квартира 47 кв.м, 11 этаж
    #             В премиум корпусе  NEXT  ORANGE
    #             5 мин пешком до моря ,
    #             Все необходимое есть. Газовое отопление, Стиральная машина, Бытовая техника, wifi, кондиционер.
    #             750$ в месяц + коммунальные платежи и интернет.
    #             Оплата 1/12 месяц + возвратный депозит
    #             ул.Инасаридзе угол Кобаладзе
    #             Собственник
    #             Писать в личку
    #             @geo_neb"""}}

    with open('path', 'r') as file:
        raw_data = json.load(file)

        parse_and_add_apartments(raw_data)

    return "Added", 200

from rentogram import app, logger, db, sql_engine
from sqlalchemy.orm import Session
from urllib.parse import urljoin


class Appartment(db.Model):
    """Модель для хранения данных об играх"""

    __tablename__ = 'Appartments'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    rooms = db.Column(db.Integer)
    address = db.Column(db.String)
    area = db.Column(db.Integer)
    link = db.Column(db.String, nullable=False)

    def add_appartment(self):
        pass

    @staticmethod
    def get_apartments():
        """метод для получения всех квартир из базы данных"""
        with Session(sql_engine) as session:

            results = session.query(Appartment).all()
            appartments = []
            for result in results:
                appartment = {'id': result.id,
                              'description': result.description,
                              'price': result.price,
                              'contact': result.contact,
                              'rooms': result.rooms,
                              'address': result.address,
                              'area': result.area,
                              'link': result.link}
                appartments.append(appartment)

            return appartments

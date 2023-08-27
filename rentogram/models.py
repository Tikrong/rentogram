from rentogram import app, logger, db, sql_engine
from sqlalchemy.orm import Session
from urllib.parse import urljoin


class Apartment(db.Model):
    """Модель для хранения данных об играх"""

    __tablename__ = 'Apartments'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer)
    contact = db.Column(db.String)
    rooms = db.Column(db.Integer)
    address = db.Column(db.String)
    area = db.Column(db.Integer)
    link = db.Column(db.String, nullable=False)

    @staticmethod
    def add_apartments(apartments_data: list[dict]):
        with Session(sql_engine) as session:
            counter = 0
            for datum in apartments_data:
                try:
                    apartment_entry = Apartment(description=datum['description'], price=datum['price'],
                                                contact=datum['contact'], rooms=datum['rooms'], address=datum['address'],
                                                area=datum['area'], link=datum['link'])

                    session.add(apartment_entry)
                    # session.commit()
                    counter += 1

                except Exception as e:
                    logger.error(f"Couldn't add {datum} to db, got error {e}")

            session.commit()
            return counter

    @staticmethod
    def get_apartments():
        """метод для получения всех квартир из базы данных"""
        with Session(sql_engine) as session:

            results = session.query(Apartment).all()
            apartments = []
            for result in results:
                appartment = {'id': result.id,
                              'description': result.description,
                              'price': result.price,
                              'contact': result.contact,
                              'rooms': result.rooms,
                              'address': result.address,
                              'area': result.area,
                              'link': result.link}
                apartments.append(appartment)

            return apartments

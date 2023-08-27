import openai
import json
import time

from urllib.parse import urljoin

from rentogram import app
from rentogram.models import Apartment


def parse_and_add_apartments(raw_data: dict):

    """
    Сюда придет json
    {Название_канала: [{"id сообщения": "  Сообщение", "id сообщения": "  Сообщение", "id сообщения": "  Сообщение"}],
    Название_канала2: [{"id сообщения": "  Сообщение", "id сообщения": "  Сообщение", "id сообщения": "  Сообщение"}]}
    """

    openai.api_key = app.config.get('OPENAI_AIP_KEY')

    data = []
    cooldown = 0

    try:
        for chanel_name, messages in raw_data.items():
            print(f"Started parsing {chanel_name}")
            for message_id, message_txt in messages.items():
                if cooldown >= 2:
                    print('waiting for 60 seconds...')
                    time.sleep(60)
                    cooldown = 0

                start = time.time()
                print(f"Parsing message_id={message_id}")
                if not message_txt:
                    continue

                # проверяем, что это текст объявления
                # is_relevant_add_check = """"Похоже ли это на объявление об аренде жилья? Ответь ture или false
                #                             Менеджер по продажам (без поиска клиентов)"""
                #
                # completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                #                                           messages=[{"role": "user", "content": ":\n".join([is_relevant_add_check, message_txt])}])
                # result = completion.choices[0].message['content']
                #
                # if result == "False" or result == "false":
                #     continue
                # cooldown += 1

                get_data_we_need_request = """Напиши какая площадь квартиры (area, integer), стоимость аренды (price, integer), 
                                              адрес квартиры (address), контактный телефон или другой контакт или None если отсутствуют (contact), 
                                              сколько комнат (rooms, integer) исходя из этого текста в формате json:"""

                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                          messages=[{"role": "user", "content": ":\n".join(
                                                              [get_data_we_need_request, message_txt])}])
                result = json.loads(completion.choices[0].message['content'])
                cooldown += 1

                if not result:
                    continue

                try:
                    print(result)
                    desctiption = message_txt
                    price = result['price'] if isinstance(result['price'], int) else int(result['price'])
                    rooms = result['rooms'] if isinstance(result['rooms'], int) else int(result['rooms'])
                    area = result['area'] if isinstance(result['area'], int) else int(result['area'])
                    contact = result['contact']
                    address = result['address']
                    link = "/".join(['https://t.me', chanel_name, message_id])
                    print(f"{link}, {chanel_name, message_id}")

                    apartments_data = {'description': desctiption,
                                        'price': price,
                                        'contact': contact,
                                        'rooms': rooms,
                                        'address': address,
                                        'area': area,
                                        'link': link}

                    data.append(apartments_data)

                except Exception as e:
                    print(f"Couldn't parse {message_txt}, got error {e}")

                print(f"finished parsing message_id={message_id} in {'%.3f' % (time.time() - start)}с")
    except Exception as error:
        print(f"Couldnt finished, got exception {error}")

    return Apartment.add_apartments(data)

import os
import json
import re

from app import db, models
from datetime import datetime
import fixtures


DATE_PATTERN = re.compile(r'\d{2}/\d{2}/\d{4}')
#from sqlalchemy.sql import exists


def load_fixture(file_path):
    """
    Загружает данные из файла фикстуры
    :param file_path: Путь до файла
    :return: Данные из фикстуры, либо пустой список, если файла нет.
    """
    content = []
    if os.path.isfile(file_path):
        with open(file_path, encoding='utf8') as file:
            content = json.load(file)

    return content


def migrate_user_roles(fixture_path):
    fixture_content = load_fixture(fixture_path)

    for role in fixture_content:

        if db.session.query(models.UserRole).filter(models.UserRole.id == role['id']).first() is None:
            #аналог exists().where(models.UserRole.id == role['id'])) is False:
            new_role = models.UserRole(**role) #распаковка словаря, аналог-(id=role['id'], name=role['name']
            db.session.add(new_role)

    db.session.commit()

def migrate_users(fixture_path):
    fixture_content = load_fixture(fixture_path)

    for user in fixture_content:

        if db.session.query(models.User).filter(models.User.id == user['id']).first() is None:
            db.session.add(models.User(**user))

    db.session.commit()


def migrate_orders(fixture_path):
    fixture_content = load_fixture(fixture_path)

    for order in fixture_content:
        # Конвертация дат из формата mm/dd/YYYY в ISO-8601
        for field_name, field_value in order.items():
            if isinstance(field_value, str) and field_value.count('/') == 2:
                order[field_name] = datetime.strptime(field_value, '%m/%d/%Y').date()

        if db.session.query(models.Order).filter(models.Order.id == order['id']).first() is None:
            db.session.add(models.Order(**order))

    db.session.commit()


def migrate_offers(fixture_path):
    fixture_content = load_fixture(fixture_path)

    for offer in fixture_content:

        if db.session.query(models.Offer).filter(models.Offer.id == offer['id']).first() is None:
            db.session.add(models.Offer(**offer))

    db.session.commit()

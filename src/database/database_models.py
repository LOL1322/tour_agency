from peewee import Model, CharField, IntegerField, ForeignKeyField
from peewee import *  
import settings


db = SqliteDatabase(database=f'{settings.DATABASE_PATH}/{settings.DATABASE_NAME}')


class BaseModel(Model):
    class Meta:
        database = db


class Position(BaseModel):
    post = CharField(default='')
    power_level = IntegerField(default=0)
    class Meta:
        power_level = 0
        database = db
        identifier_field = 'post'


class User(BaseModel):
    position_id = ForeignKeyField(Position, backref='users', default=0)
    login = CharField(default='')
    password = CharField(default='')
    class Meta:
        power_level = 0
        database = db
        identifier_field = 'login'


class Country(BaseModel):
    name = CharField(default='')
    class Meta:
        power_level = 0
        database = db
        identifier_field = 'name'


class Tour(BaseModel):
    country_id = ForeignKeyField(Country, backref='tours', default=0)
    hours = IntegerField(default=0)
    price = IntegerField(default=0)
    class Meta:
        power_level = 0
        database = db
        identifier_field = 'price'


class Ticket(BaseModel):
    tour_id = ForeignKeyField(Tour, backref='tickets', default=0)
    user_id = ForeignKeyField(User, backref='tickets', default=0)
    date_start = CharField(default='')
    date_end = CharField(default='')
    class Meta:
        power_level = 0
        database = db
        identifier_field = 'date_start'
        

db_models = [User, Ticket, Position, Tour, Country]

db.create_tables(db_models)
    
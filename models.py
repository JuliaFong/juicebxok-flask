from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('locations.sqlite')

class User(UserMixin, Model):
    firstName = CharField()
    lastName = CharField()
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    location = CharField()

    # class Api( Model):
    #     term = CharField()
    #     location =CharField()

    
    class Meta:
        database = DATABASE      
        

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    print("Tables Created!")
    DATABASE.close()
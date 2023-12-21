from peewee import Model, PrimaryKeyField, DateTimeField, IntegerField,ForeignKeyField
from config import Config 
from .Seanses import Seanses
from .Places import Places

class Tickets(Model):
    ticket_number = PrimaryKeyField()
    date_created = DateTimeField()
    seanses = ForeignKeyField(Seanses)
    places =  ForeignKeyField(Places)
    payed = IntegerField()
    booking = IntegerField()
    creashed = IntegerField()

    class Meta:
        database  = Config.DATABASE
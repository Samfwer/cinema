from peewee import Model, PrimaryKeyField, ForeignKeyField, IntegerField
from config import Config 
from .Seanses import Seanses
from .SectorSaloon import SectorSaloon

class PriceForTickets(Model):
    id = PrimaryKeyField(null=False)
    seanses = ForeignKeyField(Seanses, related_name='price_for_tickets')
    sector = ForeignKeyField(SectorSaloon, related_name='price_for_tickets')
    price = IntegerField() 

    class Meta:
        database  = Config.DATABASE
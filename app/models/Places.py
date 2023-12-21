from peewee import Model, PrimaryKeyField, ForeignKeyField, IntegerField
from config import Config 
from .Saloon import Saloon

class Places(Model):
    id = PrimaryKeyField(null=False)
    saloon = ForeignKeyField(Saloon, related_name='places')
    row_number = IntegerField()
    row_place = IntegerField()

    class Meta:
        database  = Config.DATABASE
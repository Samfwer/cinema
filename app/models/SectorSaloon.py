from peewee import Model, PrimaryKeyField, CharField, ForeignKeyField
from config import Config 
from .Saloon import Saloon

class SectorSaloon(Model):
    id_sector = PrimaryKeyField(null=False)
    saloon = ForeignKeyField(Saloon, related_name='sector_saloon')
    name = CharField(null=False, max_length=25)
    description = CharField(null=False, max_length=25)

    class Meta:
        database  = Config.DATABASE
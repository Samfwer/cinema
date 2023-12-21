from peewee import Model, PrimaryKeyField, CharField
from config import Config 

class JobTitle(Model):
    id = PrimaryKeyField()
    title = CharField(null=False, max_length=25)

    class Meta:
        database  = Config.DATABASE
from peewee import Model, PrimaryKeyField, CharField, ForeignKeyField
from config import Config 
from .JobTitle import JobTitle

class Employee(Model):
    id = PrimaryKeyField(null=False)
    name = CharField(null=False, max_length=25)
    title = ForeignKeyField(JobTitle)
    passord = CharField(null=False, max_length=25)

    class Meta:
        database  = Config.DATABASE
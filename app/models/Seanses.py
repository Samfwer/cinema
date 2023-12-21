from peewee import Model, PrimaryKeyField, DateTimeField, ForeignKeyField
from config import Config 
from .movie import Movies

class Seanses(Model):
    id = PrimaryKeyField(null=False)
    date =  DateTimeField(null=False)
    time = DateTimeField(null=False)
    movie = ForeignKeyField(Movies, backref='seanses')
     
    class Meta:
        database  = Config.DATABASE
from peewee import Model, PrimaryKeyField, ManyToManyField, IntegerField,DateTimeField,ForeignKeyField
from config import Config 
from .Tickets import Tickets
from .Employee import Employee

class MovingTickets(Model):
    id  = PrimaryKeyField()
    ticket = ManyToManyField(Tickets)
    date = DateTimeField(null=False)
    operation = IntegerField()
    employee = ForeignKeyField(Employee)

    class Meta:
        database  = Config.DATABASE
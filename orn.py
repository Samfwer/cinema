from peewee import Model, SqliteDatabase,TimeField,BooleanField, DateField,PrimaryKeyField, FloatField, CharField, IntegerField, ForeignKeyField

cinema_db = SqliteDatabase('cinema.db')

class Movies(Model):
    id = PrimaryKeyField(null=False)
    name = CharField(null=False, max_length=25)
    duration = FloatField(null = False)
    rental_start_date = DateField(null=False)
    rental_finish_date = DateField(null=False)
    sales_company = CharField(null=False)

    class Meta:
        database = cinema_db

class Seanses(Model):
    id = PrimaryKeyField(null=False)
    saloon = IntegerField(null=False)
    date = DateField(null=False)
    time = TimeField(null=False)
    movie =  ForeignKeyField(Movies, null=False, related_name='Movies')

    class Meta:
        database = cinema_db

class Saloon(Model):
    id = PrimaryKeyField(null=False)
    name = CharField(null=False, max_length=25)
    count_place = IntegerField(null=False)
    description = CharField(null=False)
    number_of_rows  = IntegerField(null=False)
    number_of_places = IntegerField(null=False)

    class Meta:
        database = cinema_db

class Places(Model):
    id = PrimaryKeyField(null=False)
    saloon = CharField(null=False)
    row_number = IntegerField(null=False)
    row_place = IntegerField(null=False)

    class Meta:
        database = cinema_db

class SactorSaloon(Model):
    id_dektor = IntegerField(null=False)
    saloon = CharField(null=False)
    name = CharField(null=False, max_length=25)
    description = CharField(null=False)

    class Meta:
        database = cinema_db

class PraiceForTickets(Model):
    seanses = CharField(null=False)
    sector = IntegerField(null=False)
    price = IntegerField(null=False)

    class Meta:
        database = cinema_db

class Ticets(Model):
    ticets_namber = IntegerField(null=False) 
    date_created = DateField(null=False)
    seanses = CharField(null=False)
    places = IntegerField(null=False)
    payed = BooleanField(null=False)
    booking = BooleanField(null=False)
    creashed = BooleanField(null=False)

    class Meta:
        database = cinema_db

class MovingTicets(Model):
    id_moving_ticets = IntegerField(null=False) 
    number_ticket = IntegerField(null=False)
    date_date  = DateField(null=False)
    operation  = CharField(null=False)
    employee = CharField(null=False)

    class Meta:
        database = cinema_db

class Employees(Model):
    id = PrimaryKeyField(null=False)
    name =  CharField(null=False) 
    title  = CharField(null=False) 
    password  = CharField(null=False)

    class Meta:
        database = cinema_db


class  Job_title(Model):
    id = PrimaryKeyField(null=False)
    title  = CharField(null=False) 

    class Meta:
        database = cinema_db

Movies.create_table()
Seanses.create_table()
Saloon.create_table()
Places.create_table()
SactorSaloon.create_table()
PraiceForTickets.create_table()
Ticets.create_table()
MovingTicets.create_table()
Employees.create_table()
Job_title.create_table()









    









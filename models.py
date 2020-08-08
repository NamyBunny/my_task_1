from peewee import*
from datetime import date, datetime 


db = SqliteDatabase('people.db')


class People(Model):
    gender = CharField(max_length=20)
    title = CharField(max_length=20)
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    street_number =  IntegerField()
    street_name = CharField(max_length=50)
    city = CharField(max_length=50)
    state = CharField(max_length=50)
    country = CharField(max_length=50)
    postcode = CharField(max_length=50)
    coordinates_latitude = FloatField()
    coordinates_longitude = FloatField()
    timezone_offset = TimestampField(utc=True)
    timezone_description = CharField(max_length=100)
    email = CharField()

    dob_date = DateTimeField()
    dob_age = IntegerField()
    
    registered_date = DateTimeField()
    registered_age = DateTimeField()

    phone = IntegerField()
    cell = IntegerField()
    id_name = CharField(max_length=100)
    nat = CharField(max_length=10)

    #===============================
    uuid = CharField(max_length=100)
    username = CharField(max_length=100)
    password = CharField(max_length=100)
    salt = CharField(max_length=100)
    md5 = CharField(max_length=100)
    sha1 = CharField(max_length=100)
    sha256 = CharField(max_length=100)


    # stwórz dodatkowe pole z liczbą dni pozostałych do urodzin danej osoby
    number_of_days_before_birthday = IntegerField()

    class Meta:
        database = db




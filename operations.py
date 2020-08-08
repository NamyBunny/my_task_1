import peewee
from models import*




if __name__=='__main__':
    try:
        People.create_table()
    except peewee.InternalError as px:
        print(str(px))




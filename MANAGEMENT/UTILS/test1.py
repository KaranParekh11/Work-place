import sqlalchemy as db
from sqlalchemy import inspect
from sqlalchemy import Table, Column, Integer, String ,ForeignKey
 
engine = db.create_engine('sqlite:///test1.db', connect_args={'check_same_thread':False})
conn = engine.connect()
metadata = db.MetaData()
inspector = inspect(engine)

def create_database_tabels():
    
    if 'User' not in inspector.get_table_names():
        User = Table('User', metadata,
            Column('User_Id', String, primary_key=True, nullable=False), 
            Column('User_name', String), Column('Email', String),
            Column('DOB', String), Column('Salt', String),
            Column('Digest', String),Column('Refresh_Token', String))
       

    if 'Dishes'not in inspector.get_table_names():
        Dishes = Table('Dishes', metadata,
            Column('Dish_Id', String, primary_key=True, nullable=False),
            Column('Dish_name', String), 
            Column('Price', String),
            Column('Hotel_Id', String, ForeignKey("Hotel.Hotel_Id"), nullable=False))
       

    if 'Hotel' not in inspector.get_table_names():
        Hotel = Table('Hotel', metadata,
            Column('Hotel_Id', String, primary_key=True, nullable=False), 
            Column('Hotel_name', String), Column('Distance', String),
            Column('Star', String), Column('Time', String))
     
    metadata.create_all(engine)
create_database_tabels()
Hotel = db.Table('Hotel',metadata,autoload=True,autoload_with=engine)
User = db.Table('User',metadata,autoload=True,autoload_with=engine)
Dishes = db.Table('Dishes',metadata,autoload=True,autoload_with=engine)


 
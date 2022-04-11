import sqlalchemy as db
from sqlalchemy import inspect
from sqlalchemy import Table, Column, Integer, String , Date,Boolean,DateTime
 
engine = db.create_engine('sqlite:///flaskmail.db', connect_args={'check_same_thread':False})
conn = engine.connect()
metadata = db.MetaData()
inspector = inspect(engine)

def create_database_tabels():
    
    if 'user' not in inspector.get_table_names():
        user = Table('user', metadata,
            Column('id', String, primary_key=True, nullable=False), 
            Column('name', String), Column('email', String),
            Column('mobileno', Integer),
            Column('dob', Date), Column('salt', String),
            Column('digest', String),
            Column('otp',Integer ),Column('expire_at',DateTime),
            Column('isverify',Boolean ))
       

    
    metadata.create_all(engine)
create_database_tabels()
user = db.Table('user',metadata,autoload=True,autoload_with=engine)



 
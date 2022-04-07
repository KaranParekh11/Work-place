import sqlalchemy as db
from sqlalchemy import inspect
from sqlalchemy import Table, Column, Integer, String ,ForeignKey,Date
 
engine = db.create_engine('sqlite:///test2.db', connect_args={'check_same_thread':False})
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
            Column('digest', String),Column('refresh_Token', String))
       

    if 'product'not in inspector.get_table_names():
        product = Table('product', metadata,
            Column('id', String, primary_key=True, nullable=False),
            Column('name', String), 
            Column('price', String),
            Column('stock', String),
            Column('description', String),
            Column('company_id', String, ForeignKey("company.id"), nullable=False))
       

    if 'company' not in inspector.get_table_names():
        company = Table('company', metadata,
            Column('id', String, primary_key=True, nullable=False), 
            Column('name', String), Column('category', String),
            Column('website', String), Column('days', String),
            Column('time', String),Column('address', String))#days=working days and time = working hours
     
    metadata.create_all(engine)
create_database_tabels()
company = db.Table('company',metadata,autoload=True,autoload_with=engine)
user = db.Table('user',metadata,autoload=True,autoload_with=engine)
product = db.Table('product',metadata,autoload=True,autoload_with=engine)


 
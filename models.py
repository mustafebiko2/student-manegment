from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy


#intialize metadate
metadate = MetaData()

db = SQLAlchemy(metadata=metadate)


#define models
class students(db.Model):
    #define table
    pass
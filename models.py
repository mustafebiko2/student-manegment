from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy


#intialize metadate
metadate = MetaData()

db = SQLAlchemy(metadata=metadate)


#define models
class students(db.Model):
    #define table
    __tablename__ = "students"

    id = db.Column(db.integer, primary_key=True)
    first_name = db.Column(db.text, nullable=False)
    last_name = db.Column(db.text, nullable=False)
    email = db.Column(db.string, nullable=False)
    phone = db.Column(db.integer, nullable, unique=True)
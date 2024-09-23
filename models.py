from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy


# Initialize metadata
metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


# Define models
class Student(db.Model): 
    # Define table
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)  
    first_name = db.Column(db.String, nullable=False) 
    last_name = db.Column(db.String, nullable=False)   
    email = db.Column(db.String, nullable=False, unique=True) 
    phone = db.Column(db.String, nullable=False, unique=True)  
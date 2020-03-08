from src.database.db import db
from .Course import Course 

class Student(db.Document):
  email = db.StringField(required=True, unique=True)
  name = db.StringField(required=True, unique=True)
  date_of_birth = db.StringField(required=True)

Student.register_delete_rule(Course, 'student_ids', db.CASCADE)
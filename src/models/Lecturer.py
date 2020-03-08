from src.database.db import db
from .Course import Course 

class Lecturer(db.Document):
  name = db.StringField(required=True, unique=True)

Lecturer.register_delete_rule(Course, 'lecturer_id', db.CASCADE)
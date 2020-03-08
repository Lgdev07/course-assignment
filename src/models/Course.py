from src.database.db import db

class Course(db.Document):
  name = db.StringField(required=True, unique=True)
  capacity = db.IntField(required=True)
  lecturer_id = db.ReferenceField('Lecturer', required=True)
  student_ids = db.ListField(db.ReferenceField('Student'))

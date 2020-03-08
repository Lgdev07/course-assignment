from src.controllers.LecturerApi import LecturerApi
from src.controllers.CourseApi import CourseApi

def initialize_routes(api):
  api.add_resource(LecturerApi, '/api/lecturers')
  api.add_resource(CourseApi, '/api/courses')
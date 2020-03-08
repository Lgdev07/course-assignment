from flask import Response, request
from flask_restful import Resource

from src.models.Lecturer import Lecturer
from src.models.Course import Course

from src.resources.errors import LecturerNotExistsError, InternalServerError

class CourseApi(Resource):

  def post(self):
    try:
      body = request.get_json()
      lecturer = Lecturer.objects.get(id=body['lecturer_id'])
      import pdb; pdb.set_trace()
      if not lecturer:
        raise LecturerNotExistsError
      course = Course(**body)
      course.save()
      id = course.id
      return {'id': str(id)}, 200
    except Exception as e:
      raise InternalServerError
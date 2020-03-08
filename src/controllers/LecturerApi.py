from flask import Response, request
from flask_restful import Resource

from src.models.Lecturer import Lecturer

from src.resources.errors import InternalServerError

class LecturerApi(Resource):

  def post(self):
    try:
      body = request.get_json()
      lecturer = Lecturer(**body)
      lecturer.save()
      return Response(lecturer, mimetype='application/json', status=200)
    except Exception as e:
      raise InternalServerError

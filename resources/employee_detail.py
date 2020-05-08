from flask import Response, request
from database.models import EmployeeDetails
from flask_restful import Resource

from mongoengine.errors import DoesNotExist
from resources.errors import InternalServerError, EmployeeDetailsNotExistsError

class EmployeeDetailApi(Resource):

    def get(self, id):
        try:
            employee = EmployeeDetails.objects.get(employee_id=int(id)).to_json()
            return Response(employee, mimetype="application/json", status=200)
        except DoesNotExist:
            raise EmployeeDetailsNotExistsError
        except Exception:
            raise InternalServerError
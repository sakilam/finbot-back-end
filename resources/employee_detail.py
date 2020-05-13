from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import EmployeeDetails
from flask_restful import Resource

from mongoengine.errors import DoesNotExist
from resources.errors import InternalServerError, EmployeeDetailsNotExistsError

class EmployeeDetailApi(Resource):

    @jwt_required
    def get(self, id):
        try:
            employee_id = get_jwt_identity()
            employee = EmployeeDetails.objects.get(employee_id=employee_id).to_json()
            return Response(employee, mimetype="application/json", status=200)
        except DoesNotExist:
            raise EmployeeDetailsNotExistsError
        except Exception:
            raise InternalServerError
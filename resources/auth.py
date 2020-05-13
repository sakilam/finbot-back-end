from flask import request
from flask import Response, request
from flask_jwt_extended import create_access_token
from database.models import Employees, EmployeeDetails
from flask_restful import Resource
import datetime
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, InternalServerError

class SignupApi(Resource):

    def post(self):
        try:
            body = request.get_json()
            employee = Employees(**body)
            employee.hash_password()
            employee.save()
            id = employee.id
            employee_detail = EmployeeDetails.objects.get(personal_details__email=body.get('email'))
            employee_detail.employee_id = id
            employee_detail.save()
            return {'id': str(id)}, 200
        except DoesNotExist:
            print("Employee details not found!")
            return {'id': str(id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class LoginApi(Resource):

    def post(self):
        try:
            body = request.get_json()
            employee = Employees.objects.get(email=body.get('email'))
            authorized = employee.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(employee.id), expires_delta=expires)
            return {'token': access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError

from .employee_detail import EmployeeDetailApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(EmployeeDetailApi, '/api/employees/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
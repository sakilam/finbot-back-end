from .employee_detail import EmployeeDetailApi

def initialize_routes(api):
    api.add_resource(EmployeeDetailApi, '/api/employees/<id>')
class InternalServerError(Exception):
    pass

class EmployeeDetailsNotExistsError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "EmployeeDetailsNotExistsError": {
         "message": "Employee with given id doesn't exists",
         "status": 400
    }
}
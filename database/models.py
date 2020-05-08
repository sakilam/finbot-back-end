from .db import db

class EmployeeDetails(db.Document):
    employee_id = db.StringField()
    employee_name = db.StringField()
    email = db.StringField()
    company = db.StringField()
    joined_on = db.StringField()
    designation = db.StringField()
    pan_no = db.StringField()
    dob = db.StringField()
    type_of_job = db.StringField()
    marital_status = db.StringField()
from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

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

class Employee(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
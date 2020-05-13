from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class EmployeeDetails(db.Document):
    employee_id = db.ReferenceField('Employees')
    emp_id = db.IntField()
    personal_details = db.DictField()
    latest_pay_slip = db.DictField()
    latest_ctc = db.DictField()
    leave_balance = db.DictField()
    guest_wifi_password = db.StringField()
    it_operations_contact = db.StringField()
    hr_contact = db.StringField()
    claim_form_links = db.StringField()
    tax_slab_chosen = db.StringField()
    tax_slab = db.DictField()
    project = db.StringField()
    reporting_manager = db.StringField()

class Employees(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
import uuid
from db import db
from datetime import datetime
import marshmallow as ma
from models.account_app_user_association import association_table

class Accounts(db.Model):
    __tablename__ = 'Accounts'

    account_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    parent_account_id = db.Column(UUID(as_uuid=True), default=None)
    name = db.Column(db.String(), unique=True, nullable=False)
    address = db.Column(db.String(), unique=True, nullable=False)
    city = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    zip_code = db.Column(db.String(), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    sub_accounts = db.Column(db.Integer, nullable=False, default=0)
    pending_projects = db.Column(db.Integer, nullable=False, default=0)
    on_hold_projects = db.Column(db.Integer, nullable=False, default=0)
    completed_projects = db.Column(db.Integer, nullable=False, default=0)
    
    account_manager_id = db.Column(UUID(as_uuid=True), db.ForeignKey('AppUsers.user_id'), nullable=True)
    projects = db.relationship('Projects', backref=db.backref('account'))
    clients =db.relationship('AppUsers', secondary=association_table, back_populates='accounts')


    def __init__(self, name, address, city, state, zip_code, account_manager_id, parent_account_id, sub_accounts, pending_projects, on_hold_projects, completed_projects):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.account_manager_id = account_manager_id
        self.parent_account_id = parent_account_id
        self.sub_accounts = sub_accounts
        self.pending_projects = pending_projects
        self.on_hold_projects = on_hold_projects
        self.completed_projects = completed_projects
class AccountsSchema(ma.Schema):
    projects = ma.fields.Nested('ProjectsJobsSchema', many=True, exclude=['account_id',])
    clients = ma.fields.Nested('AppUsersSchema', many=True, only=['user_id', 'email', 'role', 'first_name', 'last_name'])
    class Meta:
        fields = ['account_id','parent_account_id', 'name', 'address', 'city', 'state', 'zip_code', 'projects', 'clients', 'account_manager_id', 'sub_accounts', 'pending_projects', 'on_hold_projects', 'completed_projects']

account_schema = AccountsSchema()
accounts_schema = AccountsSchema(many=True)

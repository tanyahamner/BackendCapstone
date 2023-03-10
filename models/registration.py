from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from db import db
import marshmallow as ma


class Registrations(db.Model):
    __tablename__= "Registrations"
    registration_id = db.Column(db.Integer(), primary_key=True,  nullable=False, default=True)
   
   
    association = db.Column(db.String())


    active = db.Column(db.Boolean(), nullable=False, default=True)

    flocks = db.relationship('Sheeps', back_populates='registry_name')

    def __init__(self, registration_id, association, active):
        self.registration_id = registration_id
     
        self.association = association
        
        self.active = active
   

class RegistrationsSchema(ma.Schema):

    class Meta:
        fields = ['registration_id', 'association',  'active']


registration_schema = RegistrationsSchema()
registrations_schema = RegistrationsSchema(many=True)


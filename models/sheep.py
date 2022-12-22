from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from db import db
import marshmallow as ma

from .registration import Registrations, RegistrationsSchema

class Sheeps(db.Model):
    __tablename__= "Sheeps"
    ear_tag_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable = False)
    scrapie_tag = db.Column(db.String(), nullable = False, unique = True)
    sex = db.Column(db.String())

    active = db.Column(db.Boolean(), nullable=False, default=True)

    registration_id = db.Column(db.ForeignKey('Registrations.registration_id'), nullable=True)
    registry_name = db.relationship('Registrations', back_populates='flocks')



    def __init__(self, ear_tag_id, name, scrapie_tag, sex, active):
        self.ear_tag_id = ear_tag_id
        self.name = name
        self.scrapie_tag = scrapie_tag
        self.sex = sex
        
        self.active = active
   

class SheepsSchema(ma.Schema):
    class Meta:
        fields = ['ear_tag_id', 'name', 'scrapie_tag',  'sex',  'active', 'registration_id', 'registry_name', 'pasture_id', 'pasture_name']

    registry_name = ma.fields.Nested(RegistrationsSchema(only=('registration_id', 'association')))
  

sheep_schema = SheepsSchema()
sheeps_schema = SheepsSchema(many=True)
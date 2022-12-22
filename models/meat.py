from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from db import db
import marshmallow as ma


class Meats(db.Model):
    __tablename__= "Meats"
    meat_id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    # ear_tag_id = db.Column(db.Integer(), foreign_key=True, unique=True, nullable=False)
    pounds = db.Column(db.String(), nullable = False)
    lambchops = db.Column(db.Integer(), nullable = False)
    burgers = db.Column(db.String(), nullable = False)
    roast = db.Column(db.String(), nullable = False)
    leg_of_lamb = db.Column(db.String(), nullable = False)
    shoulderchops= db.Column(db.String(), nullable = False)
    shanks = db.Column(db.String(), nullable = False)
 
   

    active = db.Column(db.Boolean(), nullable=False, default=True)

    def __init__(self, meat_id, ear_tag_id, pounds, lambchops, burgers, roast, leg_of_lamb, shoulderchops, shanks, active):
        self.meat_id = meat_id
        self.ear_tag_id = ear_tag_id
        self.pounds = pounds
        self.lambchops = lambchops
        self.burgers = burgers
        self.roast = roast
        self.leg_of_lamb = leg_of_lamb
        self.shoulderchops = shoulderchops
        self.shanks = shanks

        self.active = active

class MeatsSchema(ma.Schema):
    class Meta:
        fields = ['meat_id', 'ear_tag_id', 'pounds', 'lambchops', 'burgers', 'roast', 'leg_of_lamb', 'shoulderchops', 'shanks', 'active']
  
meat_schema = MeatsSchema()
meats_schema = MeatsSchema(many=True)
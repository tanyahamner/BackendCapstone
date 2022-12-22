from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from db import db
import marshmallow as ma


class Wools(db.Model):
    __tablename__= "Wools"
    wool_id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    # ear_tag_id = db.Column(db.Integer(), foreign_key=True, unique=True, nullable=False)
    staple_length = db.Column(db.String(), nullable = False)
    micron = db.Column(db.Integer(), nullable = False)
    color = db.Column(db.String(), nullable = False)
    ear_tag_id = db.Column(db.String(), nullable = False)
    shear_date = db.Column(db.String(), nullable = False)
    fleece_weight= db.Column(db.String(), nullable = False)
    shear_cost = db.Column(db.String(), nullable = False)
    fleece_price = db.Column(db.DateTime, default=datetime.utcnow)
 
   

    active = db.Column(db.Boolean(), nullable=False, default=True)

    def __init__(self, wool_id, staple_length, micron, color, ear_tag_id, shear_date, fleece_weight, shear_cost, fleece_price, active):
        self.wool_id = wool_id
        self.staple_length = staple_length
        self.micron = micron
        self.color = color
        self.ear_tag_id = ear_tag_id
        self.shear_date = shear_date
        self.fleece_weight = fleece_weight
        self.shear_cost = shear_cost
        self.fleece_price = fleece_price

        self.active = active

class WoolsSchema(ma.Schema):
    class Meta:
        fields = ['wool_id', 'staple_length', 'micron', 'color', 'ear_tag_id', 'shear_date', 'fleece_weight', 'shear_cost', 'fleece_price', 'active']
  
wool_schema = WoolsSchema()
wools_schema = WoolsSchema(many=True)
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from db import db
import marshmallow as ma


class Purchases(db.Model):
    __tablename__= "Purchases"
    purchase_id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    # customer_id = db.Column(db.Integer(), foreign_key=True, unique=True, nullable=False)
    wool_id = db.Column(db.String(), nullable = False)
    meat_id = db.Column(db.Integer(), nullable = False)
    date = db.Column(db.String(), nullable = False)
    
    active = db.Column(db.Boolean(), nullable=False, default=True)

    def __init__(self, purchase_id, customer_id, wool_id, meat_id, date, active):
        self.purchase_id = purchase_id
        self.customer_id = customer_id
        self.wool_id = wool_id
        self.meat_id = meat_id
        self.date = date
        
        self.active = active

class PurchasesSchema(ma.Schema):
    class Meta:
        fields = ['purchase_id', 'customer_id', 'wool_id', 'meat_id', 'date','active']
  
purchase_schema = PurchasesSchema()
purchases_schema = PurchasesSchema(many=True)


from db import db

from lib.authenticate import authenticate
from flask import Flask, request, Response, jsonify

from models.purchase import Purchases, purchases_schema


@authenticate
def purchase_add(request):
    post_data = request.json

    if not post_data:
      post_data = request.post
    
    purchase_id = post_data.get('purchase_id')
    customer_id = post_data.get('customer_id')
    meat_id = post_data.get('meat_id')
    date = post_data.get('date')
    
    active = post_data.get('active')

    add_purchase(purchase_id, customer_id, meat_id, date, active)

    return jsonify("purchase created"), 201


def add_purchase(purchase_id, customer_id, meat_id, date, active): 
    new_purchase = Purchases(purchase_id, customer_id, meat_id, date, active)
    
    db.session.add(new_purchase)
    db.session.commit()

@authenticate
def get_purchases(request):
    results = db.session.query(Purchases).filter(Purchases.active == True).all()

    if results:
      return jsonify(purchases_schema.dump(results)), 200
    
    else:
      return jsonify('No purchase Found'), 404


@authenticate
def purchase_update(request):
    post_data = request.get_json()
    purchase_id = post_data.get("purchase_id")
    customer_id = post_data.get("customer_id")
    meat_id = post_data.get("meat_id")
    date = post_data.get('date')
    
    active = post_data.get('active')

    if active == None:
      active = True
      
      purchase_data = None

      if purchase_id != None:
        purchase_data = db.session.query(Purchases).filter(Purchases.purchase_id == purchase_id).first()

      if purchase_data:
        purchase_id = purchase_data.purchase_id
        if customer_id:
          purchase_data.customer_id = customer_id
        if meat_id is not None:
          purchase_data.meat_id = meat_id
        if date is not None:
          purchase_data.date = date
        
        if active is not None:
          purchase_data.active = active

        db.session.commit()

        return jsonify('purchase Information Updated'), 200
      else:
        return jsonify("purchase Not Found"), 404
    else:
      return jsonify("ERROR: request must be in JSON format"), 400


@authenticate
def purchase_delete(purchase_id):
    results = db.session.query(Purchases).filter(Purchases.purchase_id == purchase_id).first()
    db.session.delete(results)
    db.session.commit()
    return jsonify('purchase Deleted'), 200


from db import db

from lib.authenticate import authenticate
from flask import Flask, request, Response, jsonify

from models.wool import Wools, wools_schema


@authenticate
def wool_add(request):
    post_data = request.json

    if not post_data:
      post_data = request.post
    
    wool_id = post_data.get('wool_id')
    staple_length = post_data.get('staple_length')
    micron = post_data.get('micron')
    color = post_data.get('color')
    ear_tag_id = post_data.get('ear_tag_id')
    shear_date = post_data.get('shear_date')
    fleece_weight = post_data.get('fleece_weight')
    shear_cost = post_data.get('shear_cost')
    fleece_price = post_data.get('fleece_price')
    
    active = post_data.get('active')

    add_wool(wool_id, staple_length, micron, color, ear_tag_id, shear_date, fleece_weight, shear_cost, fleece_price, active)

    return jsonify("wool created"), 201


def add_wool(wool_id, staple_length, micron, color, ear_tag_id, shear_date, fleece_weight, shear_cost, fleece_price, active): 
    new_wool = Wools(wool_id, staple_length, micron, color, ear_tag_id, shear_date, fleece_weight, shear_cost, fleece_price, active)
    
    db.session.add(new_wool)
    db.session.commit()

@authenticate
def get_wools(request):
    results = db.session.query(Wools).filter(Wools.active == True).all()

    if results:
      return jsonify(wools_schema.dump(results)), 200
    
    else:
      return jsonify('No wool Found'), 404


@authenticate
def wool_update(request):
    post_data = request.get_json()
    wool_id = post_data.get("wool_id")
    staple_length = post_data.get("staple_length")
    micron = post_data.get("micron")
    color = post_data.get('color')
    ear_tag_id = post_data.get('ear_tag_id')
    shear_date = post_data.get('shear_date')
    fleece_weight = post_data.get('fleece_weight')
    shear_cost = post_data.get('shear_cost')
    fleece_price = post_data.get('fleece_price')

    active = post_data.get('active')

    if active == None:
      active = True
      
      wool_data = None

      if wool_id != None:
        wool_data = db.session.query(Wools).filter(Wools.wool_id == wool_id).first()

      if wool_data:
        wool_id = wool_data.wool_id
        if staple_length:
          wool_data.staple_length = staple_length
        if micron is not None:
          wool_data.micron = micron
        if color is not None:
          wool_data.color = color
        if ear_tag_id is not None:
          wool_data.ear_tag_id = ear_tag_id
        if shear_date is not None:
          wool_data.shear_date = shear_date
        if fleece_weight is not None:
          wool_data.fleece_weight = fleece_weight
        if shear_cost is not None:
          wool_data.shear_cost = shear_cost
        if fleece_price is not None:
          wool_data.fleece_price = fleece_price

        if active is not None:
          wool_data.active = active

        db.session.commit()

        return jsonify('wool Information Updated'), 200
      else:
        return jsonify("wool Not Found"), 404
    else:
      return jsonify("ERROR: request must be in JSON format"), 400


@authenticate
def wool_delete(wool_id):
    results = db.session.query(Wools).filter(Wools.wool_id == wool_id).first()
    db.session.delete(results)
    db.session.commit()
    return jsonify('wool Deleted'), 200
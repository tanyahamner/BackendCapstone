

from db import db

from lib.authenticate import authenticate
from flask import Flask, request, Response, jsonify

from models.meat import Meats, meats_schema


@authenticate
def meat_add(request):
    post_data = request.json

    if not post_data:
      post_data = request.post
    
    meat_id = post_data.get('meat_id')
    ear_tag_id = post_data.get('ear_tag_id')
    pounds = post_data.get('pounds')
    lambchops = post_data.get('lambchops')
    burgers = post_data.get('burgers')
    roast = post_data.get('roast')
    leg_of_lamb = post_data.get('leg_of_lamb')
    shoulderchops = post_data.get('shoulderchops')
    shanks = post_data.get('shanks')

    active = post_data.get('active')

    add_meat(meat_id, ear_tag_id, pounds, lambchops, burgers, roast, leg_of_lamb, shoulderchops, shanks,  active)

    return jsonify("meat created"), 201


def add_meat(meat_id, ear_tag_id, pounds, lambchops, burgers, roast, leg_of_lamb, shoulderchops, shanks,  active): 
    new_meat = Meats(meat_id, ear_tag_id, pounds, lambchops, burgers, roast, leg_of_lamb, shoulderchops, shanks,  active)
    
    db.session.add(new_meat)
    db.session.commit()

@authenticate
def get_meats(request):
    results = db.session.query(Meats).filter(Meats.active == True).all()

    if results:
      return jsonify(meats_schema.dump(results)), 200
    
    else:
      return jsonify('No meat Found'), 404


@authenticate
def meat_update(request):
    post_data = request.get_json()
    meat_id = post_data.get("meat_id")
    ear_tag_id = post_data.get("ear_tag_id")
    pounds = post_data.get("pounds")
    lambchops = post_data.get('lambchops')
    burgers = post_data.get('burgers')
    roast = post_data.get('roast')
    leg_of_lamb = post_data.get('leg_of_lamb')
    shoulderchops = post_data.get('shoulderchops')
    shanks = post_data.get('shanks')

    active = post_data.get('active')

    if active == None:
      active = True
      
      meat_data = None

      if meat_id != None:
        meat_data = db.session.query(Meats).filter(Meats.meat_id == meat_id).first()

      if meat_data:
        meat_id = meat_data.meat_id
        if ear_tag_id:
          meat_data.ear_tag_id = ear_tag_id
        if pounds is not None:
          meat_data.pounds = pounds
        if lambchops is not None:
          meat_data.lambchops = lambchops
        if burgers is not None:
          meat_data.burgers = burgers
        if roast is not None:
          meat_data.roast = roast
        if leg_of_lamb is not None:
          meat_data.leg_of_lamb = leg_of_lamb
        if shoulderchops is not None:
          meat_data.shoulderchops = shoulderchops
        if shanks is not None:
          meat_data.shanks = shanks

        if active is not None:
          meat_data.active = active

        db.session.commit()

        return jsonify('meat Information Updated'), 200
      else:
        return jsonify("meat Not Found"), 404
    else:
      return jsonify("ERROR: request must be in JSON format"), 400


@authenticate
def meat_delete(ear_tag_id):
    results = db.session.query(Meats).filter(Meats.ear_tag_id == ear_tag_id).first()
    db.session.delete(results)
    db.session.commit()
    return jsonify('meat Deleted'), 200
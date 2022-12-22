from db import db

from lib.authenticate import authenticate, authenticate_return_auth, validate_auth_token
from flask import Flask, request, Response, jsonify

from models.sheep import Sheeps, sheeps_schema, sheep_schema


@authenticate
def sheep_add(request):
    post_data = request.json

    if not post_data:
      post_data = request.post
    
    ear_tag_id = post_data.get('ear_tag_id')
    name = post_data.get('name')
    scrapie_tag = post_data.get('scrapie_tag')
    sex = post_data.get('sex')
    # registration_id = post_data.get('registration_id')
    active = post_data.get('active')

    add_sheep(ear_tag_id, name, scrapie_tag, sex,  active)

    return jsonify("sheep created"), 201


def add_sheep(ear_tag_id, name, scrapie_tag, sex,  active): 
    new_sheep = Sheeps(ear_tag_id, name, scrapie_tag, sex,  active)
    
    db.session.add(new_sheep)
    db.session.commit()

@authenticate
def get_sheeps(request):
    results = db.session.query(Sheeps).filter(Sheeps.active == True).all()

    if results:
      return jsonify(sheeps_schema.dump(results)), 200
    
    else:
      return jsonify('No sheep Found'), 404

@authenticate
def get_sheep_by_id(request, ear_tag_id):
    results = db.session.query(Sheeps).filter(Sheeps.active == True).filter(Sheeps.ear_tag_id==ear_tag_id).first()

    if results:
      return jsonify(sheep_schema.dump(results)), 200
    
    else:
      return jsonify('No sheep Found'), 404


@authenticate
def sheep_update(request):
    post_data = request.get_json()
    ear_tag_id = post_data.get("ear_tag_id")
    if ear_tag_id == None:
        return jsonify("ERROR: ear_tag_id missing"), 400
    name = post_data.get('name')
    scrapie_tag = post_data.get('scrapie_tag')
    sex = post_data.get('sex')
    registration_id = post_data.get('registration_id')
    active = post_data.get('active')
    pasture_id = post_data.get('active')
    registration_id = post_data.get('registration_id')

    if active == None:
      active = True
      
      sheep_data = None

      if ear_tag_id != None:
        sheep_data = db.session.query(Sheeps).filter(Sheeps.ear_tag_id == ear_tag_id).first()

      if sheep_data:
        ear_tag_id = sheep_data.ear_tag_id
        if name:
          sheep_data.name = name
        if scrapie_tag is not None:
          sheep_data.scrapie_tag = scrapie_tag
        if sex is not None:
          sheep_data.sex = sex
        if registration_id is not None:
          sheep_data.registration_id = registration_id
   

        if active is not None:
          sheep_data.active = active

        if registration_id !=None or registration_id != '':
            sheep_data.registration_id = registration_id

       

        db.session.commit()

        return jsonify('sheep Information Updated'), 200
      else:
        return jsonify("sheep Not Found"), 404
    else:
      return jsonify("ERROR: request must be in JSON format"), 400


@authenticate
def sheep_delete(ear_tag_id):
    results = db.session.query(Sheeps).filter(Sheeps.ear_tag_id == ear_tag_id).first()
    db.session.delete(results)
    db.session.commit()
    return jsonify('sheep Deleted'), 200
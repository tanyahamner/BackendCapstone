from db import db
from flask import jsonify
import flask
from lib.authenticate import authenticate, authenticate_return_auth, validate_auth_token
from flask import Flask, request, Response, jsonify

from models.registration import Registrations, registrations_schema, registration_schema

# @authenticate
# def add_registrations(req:flask.Request) -> flask.Response:
#   post_data = req.get_jsonify()
#   association = post_data.get('association')
  

#   record = Registrations(association)
#   db.session.add(record)
#   db.session.commit()  

#   return jsonify(registration_schema.dump(record))
@authenticate
def registration_add(request):
    post_data = request.json

    if not post_data:
      post_data = request.post
    
    registration_id = post_data.get('registration_id')
  

    association = post_data.get('association')
   
    active = post_data.get('active')
    # if active == None:
    #     active = True
    # record = Registrations(registration_id, association)

    add_registration(registration_id, association, active)

    return jsonify("registration created"), 201
  


def add_registration(registration_id,  association,  active): 
    new_registration = Registrations(registration_id, association,  active)
    
    db.session.add(new_registration)
    db.session.commit()

@authenticate
def get_registrations(request):
    results = db.session.query(Registrations).filter(Registrations.active == True).all()

    if results:
      return jsonify(registrations_schema.dump(results)), 200
    
    else:
      return jsonify('No registration Found'), 404

@authenticate
def get_registration_by_id(request, registration_id):
    results = db.session.query(Registrations).filter(Registrations.active == True).filter(Registrations.registration_id==registration_id).first()

    if results:
      return jsonify(registration_schema.dump(results)), 200
    
    else:
      return jsonify('No registration Found'), 404


@authenticate
def registration_update(request):
    post_data = request.get_json()
    registration_id = post_data.get("registration_id")
    if registration_id == None:
        return jsonify("ERROR: registration_id missing"), 400
   
    association = post_data.get('association')
    
    active = post_data.get('active')

    if active == None:
      active = True
      
      registration_data = None

      if registration_id != None:
        registration_data = db.session.query(Registrations).filter(Registrations.registration_id == registration_id).first()

      if registration_data:
        registration_id = registration_data.registration_id
        
        if association is not None:
          registration_data.association = association
       
        if active is not None:
          registration_data.active = active

        db.session.commit()

        return jsonify('registration Information Updated'), 200
      else:
        return jsonify("registration Not Found"), 404
    else:
      return jsonify("ERROR: request must be in JSON format"), 400


@authenticate
def registration_delete(registration_id):
    results = db.session.query(Registrations).filter(Registrations.registration_id == registration_id).first()
    db.session.delete(results)
    db.session.commit()
    return jsonify('registration Deleted'), 200

# from db import db

# from lib.authenticate import authenticate
# from flask import Flask, request, Response, jsonify

# from models.registration import Registrations, registrations_schema, registration_schema


# @authenticate
# def registration_add(request):
#     post_data = request.json

#     if not post_data:
#       post_data = request.post
    
#     registration_id = post_data.get('registration_id')
#     association = post_data.get('association')
    

#     active = post_data.get('active')


#     add_registration(registration_id, association, active )

#     return jsonify("registration created"), 201


# def add_registration(registration_id, association, active): 
#     new_registration = Registrations(registration_id, association, active )
    
#     db.session.add(new_registration)
#     db.session.commit()

# @authenticate
# def get_registrations(request):
#     results = db.session.query(Registrations).filter(Registrations.active == True).all()

#     if results:
#       return jsonify(registrations_schema.dump(results)), 200
    
#     else:
#       return jsonify('No Registration Found'), 404

# @authenticate
# def get_registration_by_id(request, registration_id):
#     results = db.session.query(Registrations).filter(Registrations.active == True).filter(Registrations.registration_id==registration_id).first()


#     if results:
#       return jsonify(registration_schema.dump(results)), 200
    
#     else:
#       return jsonify('No Registration Found'), 404

# @authenticate
# def registration_update(request):
#     post_data = request.get_json()
#     registration_id = post_data.get("registration_id")
#     if registration_id == None:
#         return jsonify("ERROR: registration_id missing"), 400
#     association = post_data.get('association')
#     registration_id = post_data.get('registration_id')
#     # date_registered = post_data.get('date_registered')
  
   
#     active = post_data.get('active')

#     if active == None:
#       active = True
      
#       registration_data = None

#       if registration_id != None:
#         registration_data = db.session.query(Registrations).filter(Registrations.registration_id == registration_id).first()

#       if registration_data:
#         registration_id = registration_data.registration_id
#         if association:
#           registration_data.association = association
#         # if date_registered is not None:
#         #   Registration_data.date_registered = date_registered
#         if registration_id is not None:
#           registration_data.registration_id = registration_id
     
#         if active is not None:
#           registration_data.active = active

#         db.session.commit()

#         return jsonify('Registration Information Updated'), 200
#       else:
#         return jsonify("Registration Not Found"), 404
#     else:
#       return jsonify("ERROR: request must be in JSON format"), 400


# @authenticate
# def registration_delete(registration_id):
#     results = db.session.query(Registrations).filter(Registrations.registration_id == registration_id).first()
#     db.session.delete(results)
#     db.session.commit()
#     return jsonify('Registration Deleted'), 200
# from db import db
# from sqlalchemy.dialects.postgresql import UUID
# import marshmallow as ma

# sheep_registration_association_table = db.Table(
#   "SheepRegistrationAssociation",
#   db.Model.metadata,
#   db.Column('registration_id', db.ForeignKey('Registrations.registration_id'), primary_key=True),
#   db.Column('ear_tag_id', db.ForeingKey('Sheeps.ear_tag_id'), primary_key=True)
# )

# class SheepRegistrationAssociationSchema(ma.Schema):
#   class Meta:
#     fields = ['registration_id', 'ear_tag_id']

# sheep_registration_schema = SheepRegistrationAssociationSchema()
# sheeps_registration_schema = SheepRegistrationAssociationSchema(many=True)
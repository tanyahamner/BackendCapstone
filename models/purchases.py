from sqlalchemy.dialects.postgresql import UUID
import uuid
from db import db
import marshmallow as ma

association_table = db.Table(
    "AccountAppUsersAssociation",
    db.Model.metadata,
    db.Column("user_id", db.ForeignKey("AppUsers.user_id"), primary_key=True),
    db.Column("account_id", db.ForeignKey("Accounts.account_id"), primary_key=True),
)
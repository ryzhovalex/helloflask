""" 
Database models logic.
"""

from .model_aliases import *


# CONSTRAINT EXAMPLE: https://www.youtube.com/watch?v=lnfrcHdE_HI
# check = db.Column(db.Integer, db.CheckConstraint("check<5"))

# source: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# many-to-many table
user_addresses_table = table("user_addresses", 
    column("address_id", integer(), foreign_key("address.id"), primary_key=True),
    column("user_id", integer(), foreign_key("user.id"), primary_key=True)
)


class User(model()):
    # check constraint 'age'
    __table_args__ = (
        check_constraint("age >= 18 AND age <= 80"),
    )

    id = column(integer(), primary_key=True)
    name = column(string(80), unique=True, nullable=False)
    age = column(integer(), nullable=False)

    # one-to-one connection, because 'uselist=False'
    account = db.relationship("Account", backref="user", lazy=True, uselist=False)
    # 'backref="user"' means that by calling 'Account.user' we will get this User instance

    # one-to-many connection
    order = db.relationship("Order", backref="user", lazy=True)

    # many-to-many connection
    addresses = db.relationship("Address", secondary=user_addresses_table, lazy="subquery", backref=backref("users_residents", lazy=True))
    # 'secondary' is a pointer to a table with Users and their Addresses

    def __repr__(self):
        return "<User %r>" % self.name


class Account(model()):
    """ One-to-one with User """
    id = column(integer(), primary_key=True)
    user_id = column(integer(), foreign_key("user.id"), nullable=False) # chain Account to owner-user by defining foreign key with User id
    nickname = column(string(80), nullable=False)


class Order(model()):
    """ One-to-many with User (1 user => many orders) """
    id = column(integer(), primary_key=True)
    user_id = column(integer(), foreign_key("user.id"), nullable=False) 
    name = column(string(80), nullable=False)
    delivered = column(boolean(), default=False)


class Address(model()):
    """ Many-to-many with User """
    id = column(integer(), primary_key=True)
    name = column(string(80), nullable=False)

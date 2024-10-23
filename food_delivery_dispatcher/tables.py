from enum import unique
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text, types, Table, Column
from sqlalchemy.dialects import mysql
from sqlalchemy.schema import UniqueConstraint, Index
import sqlalchemy as sa
from sqlalchemy.sql.sqltypes import Float
from sqlalchemy.types import Text , LargeBinary
from .dbutil import engine


def create_all():
    Base.metadata.create_all(engine)


def recreate_all():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

Base = declarative_base()
Base.metadata.bind = engine


class Model(Base):
    __abstract__ = True
    __bind_key__ = 'logistics'


TINYINT = mysql.TINYINT(unsigned=True)
SMALLINT = mysql.SMALLINT(unsigned=True)
MEDIUMINT = mysql.MEDIUMINT(unsigned=True)
INT = mysql.INTEGER(unsigned=True)
BIGINT = mysql.BIGINT(unsigned=True)
SINT = mysql.INTEGER(unsigned=False)
SBIGINT = mysql.BIGINT(unsigned=False)
CCY = sa.Numeric(13, 2)
FLOAT = mysql.FLOAT(unsigned=False)
ENUM = mysql.ENUM("singleton")

class DeliveryDriver(Model):
    """
    The user of the delivery driver
    """
    __tablename__ = 'delivery_driver'

    id_delivery_driver = sa.Column(INT, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(50), nullable=False, unique=True)
    is_active = sa.Column(sa.Boolean, nullable=False, server_default='1')

class Fleet(Model):
    """
    A fleet containing users
    """
    __tablename__ = 'fleet'

    id_fleet = sa.Column(INT, primary_key=True, autoincrement=True)
    fleet_code = sa.Column(sa.String(50), nullable=False, unique=True)
    is_active = sa.Column(sa.Boolean, nullable=False, server_default='1')

class UserState(Model):
    """
    The user state contains the status of the user and the user's current fleet
    """
    __tablename__ = 'user_state'

    id_delivery_driver = sa.Column(INT, primary_key=True, autoincrement=True)
    id_fleet = sa.Column(INT, nullable=True)
    latitude = sa.Column(FLOAT, nullable=False)
    longitude = sa.Column(FLOAT, nullable=False)
    is_online = sa.Column(sa.Boolean, nullable=False)

class FoodOrder(Model):
    """
    The food order placed by the customer
    """
    __tablename__ = 'food_order'

    id_food_order = sa.Column(INT, primary_key=True, autoincrement=True)
    id_fleet = sa.Column(INT, nullable=False)
    order_nr = sa.Column(sa.String(50), nullable=False, unique=True)
    restaurant_latitude = sa.Column(FLOAT, nullable=False)
    restaurant_longitude = sa.Column(FLOAT, nullable=False)
    customer_latitude = sa.Column(FLOAT, nullable=False)
    customer_longitude = sa.Column(FLOAT, nullable=False)
    is_active = sa.Column(sa.Boolean, nullable=False, server_default='1')
    placed_at = sa.Column(types.TIMESTAMP, nullable=False)

class DeliveryTask(Model):
    """
    The food delivery task for a delivery driver
    """
    __tablename__ = 'delivery_task'

    id_delivery_task = sa.Column(INT, primary_key=True, autoincrement=True)
    id_food_order = sa.Column(INT, nullable=False)
    id_delivery_driver = sa.Column(INT, nullable=False)
    is_active = sa.Column(sa.Boolean, nullable=False, server_default='1')

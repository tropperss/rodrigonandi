from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///textil_production.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cnpj = Column(String, nullable=False)
    address = Column(String, nullable=False)
    contact = Column(String, nullable=False)

class Reference(Base):
    __tablename__ = 'references'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    cost = Column(Float, nullable=False)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    reference_id = Column(Integer, ForeignKey('references.id'))
    status = Column(String, nullable=False)
    reference = relationship("Reference")

class FiscalInfo(Base):
    __tablename__ = 'fiscal_infos'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    tax_info = Column(String, nullable=False)
    order = relationship("Order")

Base.metadata.create_all(engine)

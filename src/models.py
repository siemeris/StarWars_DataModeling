import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# association_table = Table(
#     "association",
#     Base.metadata,
#     Column("favoritos_id", ForeignKey("favoritos.id")),
#     Column("personajes_id", ForeignKey("personajes.id")),
# )

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nickname = Column(String(200), unique=True)
    nombre = Column(String(200), nullable=False)
    apellido = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    favoritos = relationship("favoritos")

class Favoritos(Base):
    __tablename__ = "favoritos"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    personajes_id = Column(Integer)
    planetas_id = Column(Integer)
    vehiculos_id = Column(Integer)
    usuario = relationship("usuario")  
    personajes = relationship("personajes")
    vehiculos = relationship("vehiculos")
    planetas = relationship("Planetas")

class Personajes(Base):
    __tablename__ = "personajes"
    id = Column(Integer, primary_key=True)
    personaje_id = Column(Integer) 
    nombre = Column(String(200))
    genero = Column(String(1))
    colorPelo = Column(String(150))
    colorOjos = Column(String(150))
    favoritos_id = Column(Integer, ForeignKey("favoritos.id"))
    favoritos = relationship("Favoritos")

class Planetas(Base):
    __tablename__ = "planetas"
    id = Column(Integer, primary_key=True)
    planetas_id = Column(Integer)
    nombre = Column(String(200))
    habitantes = Column(Integer)
    favoritos_id = Column(Integer, ForeignKey("favoritos.id"))
    favoritos = relationship("Favoritos")

class Vehiculos(Base):
    __tablename__ = "vehiculos"
    id = Column(Integer, primary_key=True)
    vehiculos_id = Column(Integer)
    nombre = Column(String(200))
    modelo = Column(String(200))
    fabricante = Column(String(200))
    favoritos_id = Column(Integer, ForeignKey("favoritos.id"))
    favoritos = relationship("Favoritos")


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'ModeloDatosStarWars.png')
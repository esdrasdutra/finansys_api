from sqlalchemy import Column, Integer, String

from app.db.base_class import Base

class Entrada(Base):
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(256), nullable=False)
    desc = Column(String(256), nullable=True)

class Saida(Base):
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(256), nullable=False)
    desc = Column(String(256), nullable=True)
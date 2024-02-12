from sqlalchemy import Column, Integer, String

from app.db.base_class import Base

class Dizimista(Base):
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(256), nullable=False)
    func = Column(String(256), nullable=True)
    cong = Column(String(256), nullable=True)
from sqlalchemy import Column, Integer, String

from app.db.base_class import Base

class Documento(Base):
    id = Column(Integer, primary_key=True, index=True)
    tipo_doc = Column(String(256), nullable=False)
    desc = Column(String(256), nullable=True)

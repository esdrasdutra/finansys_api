from sqlalchemy import Column, Integer, String, Date

from app.db.base_class import Base

class Obreiro(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    func = Column(String(256), nullable=False)
    cong = Column(String(256), nullable=False)
    
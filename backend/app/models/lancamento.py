from sqlalchemy import Column, Integer, String, Date
from app.db.base_class import Base
from utils import date_time

class Lancamento(Base):
    id = Column(Integer, primary_key=True, index=True)
    recibo = Column(String(256),nullable=False)
    data_lan = Column(date_time.MyDateTime, nullable=False)
    data_ven = Column(date_time.MyDateTime, nullable=False)
    tipo_doc = Column(String(256),nullable=False)
    num_doc = Column(String(256),nullable=False)
    entrada = Column(String(256),nullable=False)
    saida = Column(String(256),nullable=False)
    cong = Column(String(256),nullable=False)
    forn = Column(String(256),nullable=False)
    dizimista = Column(String(256),nullable=False)
    obs = Column(String(256),nullable=False)
    valor = Column(String(256),nullable=False)
    conta = Column(String(256),nullable=False)
    situacao = Column(String(256),nullable=False)
    tipo_lanc = Column(String(256),nullable=False)
    historico = Column(String(256),nullable=False)
    status_lanc = Column(String(256),nullable=False)
    
from sqlalchemy import Column, Integer, String, Date

from app.db.base_class import Base

class Historico(Base):
    id = Column(Integer, primary_key=True, index=True)
    lanc_recibo = Column(Integer, nullable=False)
    lanc_obs = Column(String(256), nullable=False)
    lanc_tipo_recbico = Column(String(256), nullable=False)
    lanc_nome_dizimista = Column(String(256), nullable=False)
    lanc_movimentacao = Column(String(256), nullable=False)
    lanc_cong = Column(String(256), nullable=False)
    lanc_data_lan = Column(Date, nullable=False)

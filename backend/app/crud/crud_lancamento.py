from typing import List

from sqlalchemy import asc, desc, extract, func, select
from sqlalchemy.orm import Session
from datetime import datetime

from crud.base import CRUDBase, ModelType
from models.lancamento import Lancamento
from schemas.lancamento import LancamentoCreate, LancamentoUpdate, LancamentoRemove
from schemas.paginacao import SortEnum

class CRUDlancamento(CRUDBase[Lancamento, LancamentoCreate, LancamentoUpdate, LancamentoRemove]):

    def get_all_page( self, db: Session, perPage, page, order)-> List[ModelType]:
        order = desc if order == SortEnum.DESC else asc
        print(perPage, order.__name__, page)

        query_entradas = db.query(self.model
                ).order_by(order(self.model.data_lan)
                ).filter(self.model.entrada != '-'
                ).limit(perPage
                ).offset(
                    page - 1
                    if page == 1
                    else (page - 1) * perPage
                )
        
        query_saidas = db.query(self.model
                ).order_by(order(self.model.data_lan)
                ).filter(self.model.saida != '-'
                ).limit(perPage
                ).offset(
                    page - 1
                    if page == 1
                    else (page - 1) * perPage)

        entradas = query_entradas.all()
        saidas = query_saidas.all()
        
        count = db.execute(
            select(func.count()).select_from(select(self.model.id).subquery())
        ).scalar_one()

        lancamentos_list = {
            "length": count,
            "entradas": entradas, 
            "saídas": saidas
        }
        return lancamentos_list
    
    def get_all(self, db: Session)-> List[ModelType]:
        query_entradas = db.query(
            self.model.entrada,
            extract('month', self.model.data_lan).label('mes'),
            func.sum(self.model.valor).label('valor_total')
            ).group_by(self.model.entrada, extract('month', self.model.data_lan)
            ).filter(self.model.entrada != '-')
        
        query_saidas = db.query(
            self.model.saida,
            extract('month', self.model.data_lan).label('mes'),
            func.sum(self.model.valor).label('valor_total')
            ).group_by(self.model.saida, extract('month', self.model.data_lan)
            ).filter(self.model.saida != '-')

        entradas = query_entradas.all()
        saidas = query_saidas.all()

        count = db.execute(
            select(func.count()).select_from(select(self.model.id).subquery())
        ).scalar_one()
        
        lancamentos_list = {
            "length": count,
            "entradas": entradas,
            "saidas": saidas
        }

        return lancamentos_list
    
    def get_all_crude(self, db: Session)-> List[ModelType]:
        # Data inicial e final do período
        #data_inicial = datetime(2024, 6, 1)
        #data_final = datetime(2024, 12, 31)
        print('Chamando ALL CRUDE')

        query_entradas = db.query(self.model
            ).filter(self.model.entrada != '-'
            )
        #.filter(self.model.data_lan.between(data_inicial, data_final))
        
        query_saidas = db.query(
            self.model
            #).group_by(self.model.saida, extract('month', self.model.data_lan)
            ).filter(self.model.saida != '-'
            )#.filter(self.model.data_lan > data_inicial)

        entradas = query_entradas.all()
        saidas = query_saidas.all()

        lancamentos_list = {
            "entradas": entradas,
            "saidas": saidas
        }

        return lancamentos_list
  
    ...

lancamento = CRUDlancamento(Lancamento)
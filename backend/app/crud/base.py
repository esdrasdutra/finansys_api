from typing import Annotated, Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi import Depends, Query
from fastapi.encoders import jsonable_encoder

from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc, extract, select
from datetime import date

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
RemoveSchemaType = TypeVar("RemoveSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType, RemoveSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self, db: Session)-> List[ModelType]:
        return (db.query(self.model).order_by(self.model.id).all())

    def get_multi(
        self, db: Session, *, 
        page: Optional[int] = Query(default=1, description="Page number"),
        size: Optional[int] = Query(default=10, description="Items per page")
    ) -> Page:
        query = db.query(self.model).order_by(self.model.id)
        results = paginate(query=query, )
        return results

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)

        if isinstance(obj_in, dict):
            update_data = obj_in            
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj

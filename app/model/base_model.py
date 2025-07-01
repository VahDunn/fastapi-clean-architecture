from sqlalchemy.orm import declared_attr
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime, func


class TimestampMixin:
    @declared_attr
    def created_at(cls):
        return Column(DateTime(timezone=True), server_default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class BaseModel(SQLModel, table=False):
    id: int | None = Field(default=None, primary_key=True)

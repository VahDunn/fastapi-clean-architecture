from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.util.schema import partial_model


class BaseUser(BaseModel):
    email: str
    user_token: str
    name: str
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True


class BaseUserWithPassword(BaseUser):
    password: str


class User(BaseUser):
    pass

FindUser = partial_model(BaseUser, "FindUser")
UpsertUser = partial_model(BaseUser, "UpsertUser")


class FindUserResult(BaseModel):
    founds: Optional[List[User]]
    search_options: Optional[SearchOptions]

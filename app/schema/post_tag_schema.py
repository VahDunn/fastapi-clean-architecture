# many to many schemas must be contained at one schema file to prevent cyclic reference
from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.util.schema import partial_model


# -------- Post Models --------

class BasePost(BaseModel):
    user_token: str
    title: str
    content: str
    is_published: bool

    class Config:
        from_attributes = True

class Post(ModelBaseInfo, BasePost):
    pass

FindPost = partial_model(BasePost, "FindPost")
UpsertPost = partial_model(BasePost, "UpsertPost")

class FindPostResult(BaseModel):
    founds: Optional[List[Post]]
    search_options: Optional[SearchOptions]

# -------- Tag Models --------

class BaseTag(BaseModel):
    user_token: str
    name: str
    description: str

    class Config:
        from_attributes = True

class Tag(ModelBaseInfo, BaseTag):
    pass

FindTag = partial_model(BaseTag, "FindTag")

class FindTag(FindBase, FindTag):
    id__in: Optional[str] = None

UpsertTag = partial_model(BaseTag, "UpsertTag")

class FindTagResult(BaseModel):
    founds: Optional[List[Tag]]
    search_options: Optional[SearchOptions]

# -------- Many to Many --------

class PostWithTags(Post):
    tags: Optional[List[Tag]] = None

class TagWithPosts(Tag):
    posts: Optional[List[Post]] = None

class UpsertPostWithTags(UpsertPost):
    tag_ids: Optional[List[int]] = None

class UpsertTagWithPosts(UpsertTag):
    post_ids: Optional[List[int]] = None

class FindPostWithTagsResult(BaseModel):
    founds: Optional[List[PostWithTags]]
    search_options: Optional[SearchOptions]

class FindTagWithPostsResult(BaseModel):
    founds: Optional[List[TagWithPosts]]
    search_options: Optional[SearchOptions]
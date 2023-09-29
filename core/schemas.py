from ninja import Schema
from typing import Optional,List

class TagInfo(Schema):
    value: str
    short_name: str = None

class SeedInfo(Schema):
    id: int
    col: int
    row: int
    scan_id: int
    tags: List[TagInfo]

class SeedsDataResponse(Schema):
    result: bool
    data: List[SeedInfo]
    

class TagData(Schema):
    type: str
    value: str
    deleted: bool
    short_name: str = None

class GetTagData(Schema):
    id: int
    type: str
    value: str
    deleted: bool
    short_name: str = None

class Taginfos(Schema):
    result: bool
    data: List[GetTagData]

class TagAddOut(Schema):
    result: bool
    data: TagData

class DeleteOut(Schema):
    result: bool
    message: str

class TagUpdateSchema(Schema):
    type: Optional[str] 
    value: Optional[str] 
    deleted: Optional[bool]
    short_name: Optional[str]

class TagUpdateSchemaRespnose(Schema):
    id: int
    type: str
    value: str
    deleted: bool
    short_name: str = None

class TagUpdateResponse(Schema):
    result: bool
    data: TagUpdateSchemaRespnose


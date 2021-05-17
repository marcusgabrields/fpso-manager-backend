from typing import Union
from uuid import UUID

from ninja import Schema


class Message(Schema):
    message: str


class CodeOrUUID(Schema):
    __root__: Union[str, UUID]

    # class Config:
    #     schema_extra = {
    #         "example": ["5310B9D7", "531EO9D7", "1800B9D7"]
    #     }

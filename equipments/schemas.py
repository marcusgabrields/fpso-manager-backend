from typing import Optional
from uuid import UUID

from ninja.schema import Schema

from vessels.schemas import VesselOut


class EquipamentIn(Schema):
    vessel: Optional[UUID] = None
    name: str
    code: str
    location: str

    class Config:
        schema_extra = {
            "example": {
                "name": "compressor",
                "code": "5310B9D7",
                "location": "Brazil",
            }
        }


class EquipamentOut(Schema):
    vessel: Optional[VesselOut] = None
    id: UUID
    name: str
    code: str
    location: str
    status: str

    class Config:
        schema_extra = {
            "example": {
                "vessel": {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "code": "MV102",
                },
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "compressor",
                "code": "5310B9D7",
                "location": "Brazil",
                "status": "active",
            }
        }

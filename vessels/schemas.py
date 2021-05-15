from uuid import UUID

from ninja.schema import Schema


class VesselOut(Schema):
    id: UUID
    code: str


class VesselIn(Schema):
    code: str

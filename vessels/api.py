from typing import List

from django.db.utils import IntegrityError

from ninja import Router

from common.schemas import Message

from .models import Vessel
from .schemas import VesselIn, VesselOut


router = Router()


@router.post("/", response={201: VesselOut, 409: Message}, summary="Create a Vessel")
def create_vessel(request, payload: VesselIn):
    """
    Create a **Vessel**:

    - **code**: Vessel unique code identifier.
    """
    try:
        return 201, Vessel.objects.create(**payload.dict())
    except IntegrityError:
        return 409, {"message": "Vessel code should be unique."}


@router.get("/", response=List[VesselOut], summary="List all Vessels")
def list_vessel(request):
    """
    List all **Vessels**:
    """
    return Vessel.objects.all()

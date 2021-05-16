from typing import List, Optional
from uuid import UUID

from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404

from ninja import Router

from common.schemas import Message
from equipments.models import Equipment
from equipments.schemas import EquipamentIn, EquipamentOut

from .models import Vessel
from .schemas import VesselIn, VesselOut


router = Router()


@router.post("/", response={201: VesselOut, 409: Message}, summary="Create a Vessel")
def create_vessel(request, payload: VesselIn):
    """
    Create a **Vessel**.

    - **code**: Vessel unique code identifier.
    """
    try:
        return 201, Vessel.objects.create(**payload.dict())
    except IntegrityError:
        return 409, {"message": "Vessel code should be unique."}


@router.get("/", response=List[VesselOut], summary="List all Vessels")
def list_vessel(request):
    """
    List all **Vessels**.
    """
    return Vessel.objects.all()


@router.post(
    "/{vessel_id}/equipments",
    response={201: EquipamentOut, 409: Message},
    summary="Create a Equipament in a Vessel",
)
def create_vessel_equipament(request, vessel_id: UUID, payload: EquipamentIn):
    """
    Create a **Equipament** in a **Vessel**.

    - **name**: Equipament name.
    - **code**: Equipament unique code identifier.
    - **location**: Equipament location.
    """
    vessel = get_object_or_404(Vessel, id=vessel_id)

    try:
        payload.vessel = vessel
        return 201, Equipment.objects.create(**payload.dict())
    except IntegrityError:
        return 409, {"message": "Equipament code should be unique."}


@router.get(
    "/{vessel_id}/equipments",
    response={200: List[EquipamentOut], 400: Message},
    summary="List Vessel Equipments",
)
def list_vessel_equipament(
    request,
    vessel_id: UUID,
    status: Optional[str] = None,
):
    """
    List **Vessel** **Equipments**.

    Accept filter by status
    - **status**: Equipament status, should be one of ['active', 'inactive', 'under_maintenance'].
    """
    vessel = get_object_or_404(Vessel, id=vessel_id)

    valid_status = [s.value for s in Equipment.Status]

    if status and status not in valid_status:
        return 400, {"message": f"Status should be one of {valid_status}."}

    if status:
        return 200, vessel.equipments.filter(status=status)

    return 200, vessel.equipments.all()

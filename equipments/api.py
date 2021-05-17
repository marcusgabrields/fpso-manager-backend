from ninja import Router

from common.schemas import Message

from .models import Equipment
from .schemas import SetStatusPayload


router = Router()


@router.patch(
    "/set-status",
    response={204: None, 400: Message},
    summary="Change the equipment's status",
)
def set_status(request, payload: SetStatusPayload):
    """
    Change the **equipment**'s status

    - **equipments**: Code or a list of Codes of the Equipment.
    - **status**: Equipament status, should be one of ['active', 'inactive', 'under_maintenance'].
    """
    valid_status = [s.value for s in Equipment.Status]

    if payload.status not in valid_status:
        return 400, {"message": f"Status should be one of {valid_status}."}

    queryset = Equipment.objects.all()

    if isinstance(payload.equipments, list):
        queryset.filter(code__in=payload.equipments)
    else:
        queryset.filter(code=payload.equipments)

    queryset.update(status=payload.status)

    return 204, None

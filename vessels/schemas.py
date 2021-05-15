from ninja.orm import create_schema

from .models import Vessel


VesselIn = create_schema(Vessel, fields=["code"])
VesselOut = create_schema(Vessel, fields=["code"])

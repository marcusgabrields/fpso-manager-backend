from ninja import NinjaAPI

from vessels.api import router as vessels_router


api = NinjaAPI(
    title="FPSO",
    description=(
        "A backend to manage different equipment of an FPSO "
        "(Floating Production, Storage and Offloading)."
    ),
    version="1.0.0",
)

api.add_router("/vessels/", vessels_router, tags=["vessels"])

from django.db.utils import IntegrityError
from django.test import TestCase

from ..models import Vessel


class VesselModelTest(TestCase):
    def test_can_create_a_vessel(self) -> None:
        vessel_data = {"code": "MV102"}
        Vessel.objects.create(**vessel_data)

        self.assertTrue(Vessel.objects.exists())

    def test_can_not_create_a_duplicate_code_vessel(self):
        vessel_data = {"code": "MV102"}
        Vessel.objects.create(**vessel_data)

        with self.assertRaises(IntegrityError):
            Vessel.objects.create(**vessel_data)

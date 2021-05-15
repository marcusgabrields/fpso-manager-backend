from django.db import IntegrityError
from django.test import TestCase

from model_bakery import baker

from ..models import Equipment


class EquipmentModelTest(TestCase):
    def setUp(self) -> None:
        self.vessel = baker.make("vessels.Vessel")

    def test_can_create_a_equipament(self) -> None:
        equipment_payload = {
            "vessel": self.vessel,
            "name": "compressor",
            "code": "5310B9D7",
            "location": "Brazil",
        }

        equipment = Equipment.objects.create(**equipment_payload)

        self.assertTrue(Equipment.objects.exists())
        self.assertEqual(equipment.status, Equipment.Status.ACTIVE)

    def test_can_not_create_a_duplicated_equipament(self):
        equipment_payload = {
            "vessel": self.vessel,
            "name": "compressor",
            "code": "5310B9D7",
            "location": "Brazil",
        }

        Equipment.objects.create(**equipment_payload)

        with self.assertRaises(IntegrityError):
            Equipment.objects.create(**equipment_payload)

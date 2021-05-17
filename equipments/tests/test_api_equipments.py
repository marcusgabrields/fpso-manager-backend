from django.test import TestCase

from model_bakery import baker

from ..models import Equipment


class EquipmentsSetStatusAPITest(TestCase):
    def setUp(self) -> None:
        self.content_type = "application/json"
        self.vessel = baker.make("vessels.Vessel")
        self.path = "/v1/equipments/set-status"

        self.equipment_1 = baker.make("equipments.Equipment", code="code1", vessel=self.vessel)
        self.equipment_2 = baker.make("equipments.Equipment", code="code2", vessel=self.vessel)
        self.equipment_3 = baker.make("equipments.Equipment", code="code3", vessel=self.vessel)
        self.equipment_4 = baker.make("equipments.Equipment", code="code4", vessel=self.vessel)

    def test_can_set_status_of_a_equipment_to_inactive(self) -> None:
        payload = {
            "equipments": self.equipment_1.code,
            "status": "inactive",
        }

        response = self.client.patch(self.path, data=payload, content_type=self.content_type)

        self.assertEqual(response.status_code, 204)

        self.equipment_1.refresh_from_db()
        self.assertEqual(self.equipment_1.status, Equipment.Status.INACTIVE)

    def test_can_set_status_of_an_list_of_equipments_to_inactive(self) -> None:
        payload = {
            "equipments": [
                self.equipment_1.code,
                self.equipment_2.code,
                self.equipment_3.code,
                self.equipment_4.code,
            ],
            "status": "inactive",
        }

        response = self.client.patch(self.path, data=payload, content_type=self.content_type)

        self.assertEqual(response.status_code, 204)

        self.equipment_1.refresh_from_db()
        self.equipment_2.refresh_from_db()
        self.equipment_3.refresh_from_db()
        self.equipment_4.refresh_from_db()
        self.assertEqual(self.equipment_1.status, Equipment.Status.INACTIVE)
        self.assertEqual(self.equipment_2.status, Equipment.Status.INACTIVE)
        self.assertEqual(self.equipment_3.status, Equipment.Status.INACTIVE)
        self.assertEqual(self.equipment_4.status, Equipment.Status.INACTIVE)

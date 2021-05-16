from django.test import TestCase

from model_bakery import baker

from equipments.models import Equipment


class VesselEquipmentsAPITest(TestCase):
    def setUp(self) -> None:
        self.content_type = "application/json"
        self.vessel = baker.make("vessels.Vessel")
        self.path = f"/v1/vessels/{self.vessel.id}/equipments"

    def test_can_create_a_equipament_in_a_vessel_with_a_valid_payload(self) -> None:
        equipament_payload = {
            "name": "compressor",
            "code": "5310B9D7",
            "location": "Brazil",
        }

        response = self.client.post(
            self.path, data=equipament_payload, content_type=self.content_type
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["code"], equipament_payload["code"])

    def test_can_not_create_a_duplicated_equipament_in_a_vessel(self) -> None:
        equipament_payload = {
            "name": "compressor",
            "code": "5310B9D7",
            "location": "Brazil",
        }

        expected_response = {"message": "Equipament code should be unique."}

        self.client.post(self.path, data=equipament_payload, content_type=self.content_type)
        response = self.client.post(
            self.path, data=equipament_payload, content_type=self.content_type
        )

        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json(), expected_response)


class VesselEquipmentsActiveAPITest(TestCase):
    def setUp(self) -> None:
        self.content_type = "application/json"
        self.vessel = baker.make("vessels.Vessel")
        self.path = f"/v1/vessels/{self.vessel.id}/equipments?status=active"

        baker.make("equipments.Equipment", vessel=self.vessel, _quantity=5)
        baker.make(
            "equipments.Equipment",
            vessel=self.vessel,
            status=Equipment.Status.INACTIVE,
            _quantity=5,
        )

    def test_can_list_active_vessel_equipments(self) -> None:
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)

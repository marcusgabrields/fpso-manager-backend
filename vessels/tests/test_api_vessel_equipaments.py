from django.test import TestCase

from model_bakery import baker


class VesselEquipamentsAPITest(TestCase):
    def setUp(self) -> None:
        self.content_type = "application/json"
        self.vessel = baker.make("vessels.Vessel")
        self.path = f"/v1/vessels/{self.vessel.id}/equipaments"

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

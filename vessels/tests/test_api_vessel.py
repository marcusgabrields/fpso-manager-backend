from django.test import TestCase


class VesselAPITest(TestCase):
    def setUp(self) -> None:
        self.content_type = "application/json"
        self.path = "/v1/vessels/"

    def test_can_create_a_vessel_with_a_valid_payload(self) -> None:
        vessel_payload = {"code": "MV102"}

        response = self.client.post(self.path, data=vessel_payload, content_type=self.content_type)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["code"], vessel_payload["code"])

    def test_can_not_create_a_code_duplicated_vessel(self) -> None:
        vessel_payload = {"code": "MV102"}
        expected_response = {"message": "Vessel code should be unique."}

        self.client.post(self.path, data=vessel_payload, content_type=self.content_type)
        response = self.client.post(self.path, data=vessel_payload, content_type=self.content_type)

        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json(), expected_response)

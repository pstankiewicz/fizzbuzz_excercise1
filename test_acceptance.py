from unittest import TestCase
from morelia import verify
from service import FizzBuzzService, MegaSumatorStub
from starlette.testclient import TestClient
from main import app


class FizzbuzzTestCase(TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_fizz_feature(self):
        verify('fizzbuzz.feature', self)

    def step_I_have_an_working_endpoint_fizzbuzz(self, fizzbuzz):
        r'I have an working endpoint "([^"]+)"'
        self.endpoint = fizzbuzz
        response = self.client.get(f'{fizzbuzz}')
        self.assertEqual(response.status_code, 200)

    def step_I_send_x_and_y_to_this_endpoint(self, x, y):
        r'I send (.+) and (.+) to this endpoint'

        params = {
            'first': x,
            'last': y,
        }
        self.response = self.client.get(f'{self.endpoint}', params=params)
        self.assertEqual(self.response.status_code, 200)

    def step_I_will_receive_response_in_response(self, response):
        r'I will receive (.+) in response'

        self.assertEqual(self.response.json(), {'result': response})

    def step_I_send_wrong_data_a_and_b_to_this_endpoint(self, a, b):
        r'I send wrong data "([^"]+)" and "([^"]+)" to this endpoint'

        params = {
            'first': a,
            'last': b,
        }
        self.response = self.client.get(f'{self.endpoint}', params=params)

    def step_I_will_receive_number_response_code(self, number):
        r'I will receive "([^"]+)" response code'

        self.assertEqual(self.response.status_code, 422)


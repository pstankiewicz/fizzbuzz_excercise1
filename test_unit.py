from unittest import TestCase

from service import FizzBuzzService, MegaSumatorStub


class FizzBuzzServiceTestCase(TestCase):
    def setUp(self):
        self.service = FizzBuzzService(MegaSumatorStub)

    def test_fizzbuzzservice_returns_fizz_for_sum_modulo_3(self):
        a = 5
        b = -2

        result = self.service.get(a, b)

        self.assertEqual(result, 'fizz')

    def test_fizzbuzzservice_returns_buzz_for_sum_modulo_5(self):
        a = 5
        b = 5

        result = self.service.get(a, b)

        self.assertEqual(result, 'buzz')

    def test_fizzbuzzservice_returns_fizzbuzz_for_sum_modulo_3_and_modulo_5(self):
        a = 5
        b = 10

        result = self.service.get(a, b)

        self.assertEqual(result, 'fizzbuzz')

    def test_fizzbuzzservice_returns_sum_for_sum_not_fizzbuzzetc(self):
        a = 5
        b = 2

        result = self.service.get(a, b)

        self.assertEqual(result, '7')

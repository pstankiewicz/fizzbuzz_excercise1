import requests

class MegaSumatorStub:
    def get_sum(self, a, b):
        return a + b

class MegaSumator:
    def get_sum(self, a, b):
        response = requests.get(f'https://calm-savannah-90728.herokuapp.com/?a={a}&b={b}')
        return int(response.json()['Result'])


class FizzBuzzService:
    def __init__(self, mega_sumator):
        self.mega_sumator = mega_sumator()

    def get(self, first, last):
        our_sum = self.mega_sumator.get_sum(first, last)
        if our_sum % 3 == 0 and our_sum % 5 == 0:
            return 'fizzbuzz'
        if our_sum % 5 == 0:
            return 'buzz'
        if our_sum % 3 == 0:
            return 'fizz'

        return str(our_sum)

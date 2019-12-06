Feature:
  Aby zarobic na kanapke
  Jako mega programista
  Chce spelnic wymagania biznesu dotyczace aplikacji fizzbuzz


Scenario: fizzbuzz for fizzbuzz response
  Given I have an working endpoint "/fizzbuzz/"
  When I send <x> and <y> to this endpoint
  Then I will receive <response> in response

 Examples:
    |     x |   y  | response   |
    |    30 |  -45 |   fizzbuzz |
    |    3  |   4  |   7        |
    |    0  |   5  |   buzz     |
    |    2  |   -5 |   fizz     |


Scenario: fizzbuzz for uncertain input and response
  # TODO - contact with business
  Given I have an working endpoint "/fizzbuzz/"
  When I send wrong data "a" and "b" to this endpoint
  Then I will receive "422" response code

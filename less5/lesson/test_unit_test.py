import unittest
from lesson_5 import multiplication_int, multiplication_string
from parameterized import parameterized


fixture = [
    (1, 1, 1),
    (2, 1, 2),
    (-3, -3, 9),
    (-2, 2, -4)
]
fixture_string = [
    ('A', 3, 'AAA'),
    ('Ss', 2, 'SsSs')
]


class TestFunctions(unittest.TestCase):
    # def setUp(self) -> None:
    #     print('setUp ===> START TEST')
    #
    # def tearDown(self) -> None:
    #     print('tearDown ===> END TEST')
    @parameterized.expand(fixture)
    def test_multiplication_int(self, a, b, result):
        calc_result = multiplication_int(a, b)
        self.assertEqual(calc_result, result)

    @parameterized.expand(fixture_string)
    def test_multiplication_string(self, a, b, result):
        calc_result = multiplication_string(a, b)
        self.assertEqual(calc_result, result)
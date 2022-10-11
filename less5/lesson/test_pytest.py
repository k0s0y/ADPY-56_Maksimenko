import pytest
from lesson_5 import multiplication_int, multiplication_string

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


class TestFunction2:
    def setup(self):
        ...

    def teardown(self):
        ...

    @pytest.mark.parametrize('a, b, result', fixture)
    def test_multiplication_int(self, a, b, result):
        calc_result = multiplication_int(a, b)
        assert calc_result == result

    @pytest.mark.parametrize('a, b, result', fixture_string)
    def test_multiplication_str(self, a, b, result):
        calc_result = multiplication_string(a, b)
        assert calc_result == result

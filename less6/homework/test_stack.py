import unittest
from parameterized import parameterized
from balancer import balancer
from Stack import Stack


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    brackets_balanced = [
        (True, '(((([{}]))))'),
        (True, '[([])((([[[]]])))]{()}'),
        (True, '{{[()]}}')
    ]

    brackets_unbalanced = [
        (False, '}{}'),
        (False, '{{[(])]}}'),
        (False, '[[{())}]')
    ]

    @parameterized.expand(brackets_balanced)
    def test_should_get_True_if_balanced(self, bul, brackets_list):
        self.assertEqual(balancer(brackets_list), bul)

    @parameterized.expand(brackets_unbalanced)
    def test_should_get_True_if_balanced(self, bul, brackets_list):
        self.assertEqual(balancer(brackets_list), bul)

    def test_isEmpty_should_get_True_if_list_is_empty(self):
        self.assertEqual(self.stack.isEmpty(), True)

    def test_push_and_size_should_get_1(self):
        self.stack.push('{')
        self.assertEqual(self.stack.size(), 1)


if __name__ == "__main__":
    unittest.main()

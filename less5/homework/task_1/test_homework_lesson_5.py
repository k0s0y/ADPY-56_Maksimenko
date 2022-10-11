import unittest
from app import get_doc_owner_name, get_all_doc_owners_names, get_doc_shelf, add_new_doc, \
    delete_doc, move_doc_to_shelf, add_new_shelf
from parameterized import parameterized


class TestFunctions(unittest.TestCase):

    def setUp(self) -> None:
        print("setUp --> work")

    def tearDown(self) -> None:
        print("tearDown -->work")

    def test_get_doc_owner_name(self):
        user_doc_number = "11-2"
        self.assertEqual(get_doc_owner_name(user_doc_number), "Геннадий Покемонов")

    names = [
        'Аристарх Павлов',
        'Геннадий Покемонов',
        'Василий Гупкин'
    ]
    num_of_docs = [
        ('1', '2207 876234'),
        ('1', '11-2'),
        ('2', '10006')
    ]

    @parameterized.expand(names)
    def test_get_all_doc_owners_names(self, name):
        self.assertIn(name, get_all_doc_owners_names())

    @parameterized.expand(num_of_docs)
    def test_get_doc_shelf(self, shelf, num_of_doc):
        self.assertEqual(get_doc_shelf(num_of_doc), shelf)

    def test_add_new_doc(self):
        new_doc_number = '11-22'
        new_doc_type = 'drive license'
        new_doc_owner_name = 'Igor Ivanov'
        new_doc_shelf_number = '3'
        self.assertIn(add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number), '3')
        self.assertIn(get_doc_owner_name(new_doc_number), new_doc_owner_name)

    def test_delete_doc(self):
        user_doc_number = '11-22'
        doc_owner_name = 'Igor Ivanov'
        self.assertEqual(delete_doc(user_doc_number), (user_doc_number, True))
        self.assertNotIn(doc_owner_name, get_all_doc_owners_names())

    def test_move_doc_to_shelf(self):
        user_doc_number = '10006'
        user_old_shelf_number = '1'
        user_new_shelf_number = '3'
        self.assertEqual(move_doc_to_shelf(user_doc_number, user_new_shelf_number),
                         (user_doc_number, user_new_shelf_number))
        self.assertNotEqual(get_doc_shelf(user_old_shelf_number), '1')

    def test_add_new_shelf(self):
        shelf_number = '4'
        self.assertEqual(add_new_shelf(shelf_number), (shelf_number, True))

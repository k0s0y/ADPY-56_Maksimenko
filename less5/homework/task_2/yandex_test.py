import unittest
from yandex_req import YaUploader
from Token import TOKEN


class TestYaUploader(unittest.TestCase):

    def setUp(self) -> None:
        print("setUp --> work")

    def tearDown(self) -> None:
        print("tearDown -->work")

    def test_create_folder(self):
        new_dir_name = 'test_folder'
        uploader = YaUploader(token=TOKEN)
        self.assertEqual(uploader.create_folder(new_dir_name), 201)

    def test_get_info_dir(self):
        new_dir_name = 'test_folder'
        uploader = YaUploader(token=TOKEN)
        self.assertEqual(uploader.get_info_dir(new_dir_name), ('test_folder', 'dir', 200))
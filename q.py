import unittest;
from Writer import list_process, delete_all_writers;
from WRITER_CLASS import Writer

class TestWriter(unittest.TestCase):
    def test_list_process(self):
        test_process_dictionary = {};
        self.assertEqual(0, list_process(test_process_dictionary));

    def test_delete_all_writers(self):
        test_process_dictionary = {};
        self.assertEqual(0, delete_all_writers(test_process_dictionary));

    def test_writer_bad(self):
        self.assertRaises(TypeError, Writer());
        


if __name__ == "__main__":
    unittest.main()

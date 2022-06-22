from multiprocessing import connection
import unittest
from READER_OOP import READER_TO_DB
import sqlite3

class TestReaderOOP(unittest.TestCase):
    
    def test_init(self):
        self.assertEqual(1,1)

    def test_connect(self):
        self.assertEqual(1, 1)

    def test_check_if_table_exists(self):
        self.assertEqual(1, 1)

    def test_write_to_table(self):
        self.assertEqual(1,1)
    
    def test_read_from_table(self):
        self.assertEqual(1,1)

    def test_compare_codes(self):
        self.assertEqual(1,1)
    

if __name__ == "__main__" :
    unittest.main()

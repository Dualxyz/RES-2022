from struct import Struct
import unittest
from unittest import mock 
from unittest.mock import patch
from Struct import Collection_Description;


class TestStruct(unittest.TestCase):
    
    def test_collection_description_good(self):
        self.assertRaises(TypeError, Collection_Description(1, "CODE_ANALOG", 34))
        self.assertRaises(TypeError, Collection_Description(1, "CODE_DIGITAL", 34))
        self.assertRaises(TypeError, Collection_Description(1, "CODE_LIMITSET", 34))
        self.assertRaises(TypeError, Collection_Description(1, "CODE_SINGLENOE", 34))
        self.assertRaises(TypeError, Collection_Description(1, "CODE_CONSUMER", 34))
        self.assertRaises(TypeError, Collection_Description(1, "CODE_SOURCE", 34))

    def test_collection_description_bad(self):
        self.assertRaises(TypeError, Collection_Description(1, "WRONG_CODE", 34))

    
if __name__ == '__main__':
    unittest.main()
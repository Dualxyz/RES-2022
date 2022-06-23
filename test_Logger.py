from struct import Struct
import unittest
from unittest import mock 
from unittest.mock import patch
from SEND_TO_LOG import LOG;
from Logger import SERV;
import socket;


class TestStruct(unittest.TestCase):
    def test_logger(self):
        self.assertRaises(TypeError, SERV());

if __name__ == '__main__':
    unittest.main()
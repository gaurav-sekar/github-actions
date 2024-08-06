import unittest
from functions import checkMinimumLength

class TestFunctions(unittest.TestCase):
    def test_checkMinimumLength(self):
        self.assertTrue(checkMinimumLength("FirstPassword", 10))
        self.assertTrue(checkMinimumLength("ShorterReq", 8))
        self.assertTrue(checkMinimumLength("thisismypassword", 12))

if __name__ == '__main__':
    unittest.main()

import unittest
from functions import reusePassword

class TestFunctions(unittest.TestCase):
    def test_reusePassword(self):
        self.assertFalse(reusePassword('ThisIsDefinitelyNew', ['thisisdefinite', 'hasntbeenuseDBefore', "ExtremelynewPassword", 'thisisdefinitelyneww', 'verynewpassword']))
        self.assertFalse(reusePassword('newpass', ['thisisdefinite', 'hasntbeenuseDBefore', "ExtremelynewPassword", 'thisisdefinitelyneww', 'verynewpassword']))
        self.assertFalse(reusePassword('firsttimeever', ['thisisdefinite', 'hasntbeenuseDBefore', "ExtremelynewPassword", 'thisisdefinitelyneww', 'verynewpassword']))

if __name__ == '__main__':
    unittest.main()
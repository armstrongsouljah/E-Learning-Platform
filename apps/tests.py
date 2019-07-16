import unittest

def add(a,b):
    return a + b

class Test(unittest.TestCase):
    def test_add_passes(self):
        self.assertEqual(4, add(2,2))
    
    def test_add_unexpected_numbers_fails(self):
        self.assertNotEqual(3, add(22,2))
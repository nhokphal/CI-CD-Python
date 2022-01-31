import unittest
from prime import is_prime 




class Tests(unittest.TestCase):

    def test_1(self):
        """check that 1 is not prime."""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """check that 2 is prime."""
        self.assertTrue(is_prime(2))
    def test_3(self):
        """check that 8 is the prime"""
        self.assertTrue(is_prime(8))
    def test_4(self):
        """check that 11 is the prime"""
        self.assertTrue(is_prime(11))
    def test_5(self):
        """check that 30 is the prime"""
        self.assertTrue(is_prime(29))


if __name__ == "__main__": # dont forget to call this if true, it wont show result
    unittest.main()
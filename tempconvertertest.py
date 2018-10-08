import unittest
import tempconverter as tc
import math

class TestTempConvMethods(unittest.TestCase):

    def test_zerocf(self):
        self.assertEqual(tc.ctof(0.0), 32.0)

    def test_hundredcf(self):
        self.assertEqual(tc.ctof(100), 212)

    def test_zerofc(self):
        self.assertTrue( math.isclose( tc.ftoc(0), -17.777777778) )
    
    def test_hundredfc(self):
        self.assertTrue(math.isclose( tc.ftoc(100), 37.777777778))
    

    
if __name__ == '__main__':
    unittest.main()

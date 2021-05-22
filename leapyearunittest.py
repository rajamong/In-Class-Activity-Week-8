# imports unittest functionality
import unittest
# imports leapyear class from leapyear program
from leapyear import leapyear # type: ignore

class testCase(unittest.TestCase):
    def setUp(self):
        self.leap = leapyear()

    # tests the leap year checking functionality with a valid leap year
    def test1(self):
        self.assertEqual(self.leap.checkyear(2020), (True))
    
    # tests the leap year checking functionality with an invalid leap year
    def test2(self):
        self.assertEqual(self.leap.checkyear(2011), (False))
    
    # tests the leap year checking functionality with a valid leap year
    def test3(self):
        self.assertEqual(self.leap.checkyear(2000), (True))


if __name__ == "__main__":
    unittest.main()
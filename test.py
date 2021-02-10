import unittest
import hw4

class TestWork4(unittest.testcase):

    def test_volume(self):
        self.assertEqual(volume(2),8)
        self.assertRaises(volume("x"),TypeError)
        self.assertRaises(volume(-2),ValueError)
    def test_average(self):
        self.assertEqual(average({1,2,3,4,5}),3)
        self.assertRaises(average({0,0,0}),ZeroDivisionError)
        self.assertRaises(average({}),ValueError)
    def test_fullname(self):
        self.assertEqual(fullname("Hannah","Armstrong"),"Hannah Armstrong")
        self.assertRaises(fullname(2,true),TypeError)
        self.assertEqual(fullname("1","2"),"1 2")

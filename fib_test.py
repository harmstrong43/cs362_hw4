import unittest
import fibbonacci

class test_fibbonacci(unittest.TestCase):

    def test_fibbonacci_f(self):
        self.assertEqual(fibbonacci_f(4),5)
        self.assertRaises(fibbonacci_f("x"),TypeError)
        self.assertRaises(fibbonacci_f(-2),ValueError)

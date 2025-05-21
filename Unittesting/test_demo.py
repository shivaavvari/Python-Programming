import unittest
import demo
class TestDemo(unittest.TestCase):
    def test_add(self):
        self.assertEqual(demo.add(2,2),4)
        self.assertEqual(demo.add(10,4),14)
        self.assertEqual(demo.add(23,7),30)

    def test_sub(self):
        self.assertEqual(demo.sub(10,5),5)
        self.assertEqual(demo.sub(4,5),-1)
    
    def test_mul(self):
        self.assertEqual(demo.mul(12,5),60)
        self.assertEqual(demo.mul(4,2),8)

    def test_div(self):
        self.assertEqual(demo.div(10,5),2)    
        self.assertEqual(demo.div(40,5),8)
if __name__=='__main__':
    unittest.main()

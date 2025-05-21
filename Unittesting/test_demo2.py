import unittest
import demo2

#@unittest.skip("Skipping this test for some reason")
class TestCalculate(unittest.TestCase):

    def setUp(self):
        
        self.calculate = demo2.Calculate()

    def tearDown(self):
        print("This is a teardown method, execute after test")


    def test_add(self):
        self.assertEqual(self.calculate.add(4,5),9)
    
    def test_sub(self):
        self.assertEqual(self.calculate.sub(4,5),-1)
    @unittest.skipIf(True,"Skipping because the condition is true")
    def test_mul(self):
        self.assertEqual(self.calculate.mul(4,5),20)
    
    @unittest.skipIf(True,"Skipping because the condition is true")
    def test_div(self):
        self.assertEqual(self.calculate.div(20,5),4)
        with self.assertRaises(ValueError):
            self.calculate.div(10,0)



if __name__ == '__main__':
    unittest.main()
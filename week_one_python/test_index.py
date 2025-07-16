import unittest
from index import multiply , divide , get_even_numbers

class Index_test(unittest.TestCase): 
    def test_multiply(self):
        m = multiply
        self.assertEqual(m(2,3) , 6)
        self.assertEqual(m(3,3) , 9)
    
    def test_devide(self): 
        d = divide
        self.assertEqual(d(4,2) , 2)
        self.assertEqual(d(8,4) , 2)
        zero_check = 0 
        with self.assertRaises(ZeroDivisionError):
            d(100/0)

        
    def test_get_even_numbers(self):
        e = get_even_numbers
        self.assertEqual(e([1,2,3,4]) , [2,4])
        self.assertIsInstance(e([1,2,3,4]) , list)
        
    
if __name__ == "__main__" : 
    unittest.main()
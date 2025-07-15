import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_first_numbers(self):
        g = calc.gen(10)
        self.assertEqual(next(g), 2)
        self.assertEqual(next(g), 4)
        self.assertEqual(next(g), 6)

    def test_gen(self):
        g = calc.gen(100)
        count = 0
        for _ in range(100):
            count += 2
            self.assertEqual(next(g), count)

        with self.assertRaises(StopIteration):
            next(g)

if __name__ == "__main__":
    unittest.main()

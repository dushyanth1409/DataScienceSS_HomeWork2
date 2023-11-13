import unittest
from math_quiz import mainFunc, compute, mainLogic  

class TestMainFunc(unittest.TestCase):

    def test_mainFunc(self):
        # Test with a specific range
        result = mainFunc(1, 10)
        self.assertTrue(1 <= result <= 10)

        # Test with a different range
        result = mainFunc(20, 30)
        self.assertTrue(20 <= result <= 30)

        # Test with a single value range
        result = mainFunc(5, 5)
        self.assertEqual(result, 5)

        # Test with a negative range
        result = mainFunc(-10, 0)
        self.assertTrue(-10 <= result <= 0)

        # Test with a large range
        result = mainFunc(0, 1000000)
        self.assertTrue(0 <= result <= 1000000)

class TestComputeFunction(unittest.TestCase):

    def test_compute_valid_operators(self):
        operators = set(['+', '-', '*'])
        result = compute()
        self.assertIn(result, operators)

    def test_compute_multiple_calls(self):
        operators = set(['+', '-', '*'])
        results = [compute() for _ in range(100)]
        self.assertTrue(all(op in operators for op in results))

class TestMainLogic(unittest.TestCase):

    def test_addition(self):
        result = mainLogic(3, 4, '+')
        self.assertEqual(result, ('3 + 4', 7))

    def test_subtraction(self):
        result = mainLogic(8, 2, '-')
        self.assertEqual(result, ('8 - 2', 6))

    def test_multiplication(self):
        result = mainLogic(5, 6, '*')
        self.assertEqual(result, ('5 * 6', 30))

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            mainLogic(5, 6, '/')

if __name__ == '__main__':
    unittest.main()

import random
import unittest


def mainFunc(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

    
def compute():
    return random.choice(['+', '-', '*'])


def mainLogic(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(t_q)):
        n1 = mainFunc(1, 10)
        n2 = mainFunc(1, 5)  # Change to integer range
        o = compute()

        PROBLEM, ANSWER = mainLogic(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{int(t_q)}")

# Unit Test Cases 

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

if __name__ == "__main__":
    math_quiz()
    unittest.main() 
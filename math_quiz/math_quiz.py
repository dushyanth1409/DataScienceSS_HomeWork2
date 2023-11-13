import random


def mainFunc(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

    
def compute():
    return random.choice(['+', '-', '*'])

def mainLogic(n1, n2, o):
    if o not in {'+', '-', '*'}:
        raise ValueError("Invalid operator")
    
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
        n2 = mainFunc(1, 5)
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

if __name__ == "__main__":
    math_quiz()

#משואות רמה בינונית מספרים שלמים

import random

def generate_equation():
    a = random.randint(1,10)
    c = random.randint(1,10)
    x = random.randint(-10,10)  # x can be negative now
    b = a*x
    d = c*x
    return a, b, c, d, x

def check_answer(student_answer, correct_answer):
    try:
        _, answer = student_answer.split('=')
        return int(answer.strip()) == correct_answer
    except ValueError:
        return False

def main():
    a, b, c, d, correct_answer = generate_equation()
    print(f"Solve the equation: {a}x + {b} = {c}x + {d}")
    student_answer = input("Your answer (in the form x=...): ")
    if check_answer(student_answer, correct_answer):
        print("Correct!")
    else:
        print("Incorrect!")
    print(f"The correct answer is x={correct_answer}")

if __name__ == "__main__":
    main()



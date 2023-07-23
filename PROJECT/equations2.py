#משואות בנעלם אחד רמה קלה מספרים לא שלמים
import random

def generate_equation():
    a = random.randint(1,10)
    b = random.randint(1,10)
    result = random.randint(1,10)

    # ax + b = result
    # so, x should be (result - b) / a
    x = round((result - b) / a, 2)

    return a, b, result, x

def check_answer(student_answer, correct_answer):
    if abs(student_answer - correct_answer) < 0.01: # Consider answers correct if they're within 0.01 of each other
        return True
    else:
        return False

def main():
    a, b, result, correct_answer = generate_equation()
    print(f"Solve the equation: {a}x + {b} = {result}")
    student_answer = input("Your answer (format x=value): ")

    # Parse the student answer to obtain value after "x="
    try:
        student_answer = round(float(student_answer.split('=')[1]), 2)
    except:
        print("Invalid input format!")
        return

    if check_answer(student_answer, correct_answer):
        print("Correct!")
    else:
        print("Incorrect!")
    print(f"The correct answer is x={round(correct_answer, 2)}")

if __name__ == "__main__":
    main()



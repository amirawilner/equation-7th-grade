#משואות בנעלם 1 קמה קלה מספרים שלמים
import random

def generate_equation():
    a = random.randint(1,10)
    b = random.randint(1,10)
    result = a * random.randint(1,10) + b
    # ax + b = result
    # so, x should be (result - b) / a
    x = (result - b) / a
    return a, b, result, x

def parse_student_answer(student_answer):
    try:
        _, answer = student_answer.split('=')
        return int(answer.strip())
    except (ValueError, TypeError):
        return None

def check_answer(student_answer, correct_answer):
    return student_answer == correct_answer

def main():
    a, b, result, correct_answer = generate_equation()
    print(f"Solve the equation: {a}x + {b} = {result}")
    student_answer = input("Your answer (in the format x=value): ")
    parsed_answer = parse_student_answer(student_answer)
    if parsed_answer is not None and check_answer(parsed_answer, correct_answer):
        print("Correct!")
    else:
        print("Incorrect!")
    print(f"The correct answer is x={correct_answer}")

if __name__ == "__main__":
    main()


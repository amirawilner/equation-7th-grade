#משואת רמה בינונית 
import random

def generate_equation():
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    d = random.randint(1,10)
    
    # Generate a decimal with two digits after the decimal point
    x = round(random.uniform(-10, 10), 2)
    f = a * x + b - c * d * x
    
    # Ensure f is an integer
    while not f.is_integer():
        x = round(random.uniform(-10, 10), 2)
        f = a * x + b - c * d * x

    return a, b, c, d, int(f), x

def check_answer(student_answer, correct_answer):
    return abs(student_answer - correct_answer) < 0.01 # For precision up to two decimal places

def main():
    a, b, c, d, f, correct_answer = generate_equation()
    print(f"Solve the equation: ({a}x + {b}) = {c} * ({d}x + {f})")
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



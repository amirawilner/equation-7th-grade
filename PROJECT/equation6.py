#משואות רמה קשה 
import random

def generate_equation():
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    d = random.randint(1,10)
    e = random.randint(-10,10)  # include negative values
    f = random.randint(1,10)
    g = random.randint(1,10)
    h = random.randint(1,10)
    i = random.randint(1,10)
    j = random.randint(1,10)
    k = random.randint(1,10)
    
    # Generate a decimal with two digits after the decimal point
    x = round(random.uniform(-10, 10), 2)
    l = a*x + b*(c*x+d) + e*(f*x+g) - h*(x+i) + j*(x+k)
    
    # Ensure l is an integer
    while not l.is_integer():
        x = round(random.uniform(-10, 10), 2)
        l = a*x + b*(c*x+d) + e*(f*x+g) - h*(x+i) + j*(x+k)

    return a, b, c, d, e, f, g, h, i, j, k, int(l), x

def check_answer(student_answer, correct_answer):
    return abs(student_answer - correct_answer) < 0.01 # For precision up to two decimal places

def main():
    a, b, c, d, e, f, g, h, i, j, k, l, correct_answer = generate_equation()
    print(f"Solve the equation: {a}x + {b}({c}x+{d}) + {e}({f}x+{g}) = {h}(x+{i}) - {j}(x+{k}) + {l}")
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


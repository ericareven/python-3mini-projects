import random
import time

# constant varables are in all caps
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr) # eval evaluates a string as if it is a python expression
    return expr, answer

# expr, answer = generate_problem()
# print(expr, f"= {answer}")

wrong = 0
input("Press enter to start")
print("-----------------")

start_time = time.time() # marks start time


for  i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem #{str(i+1)}: {expr} = ")
        # guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer): # convert the answer from an integer to a string bc the guess input is a string (not converting guess to integer bc the input may not be a valid int and would crash the program)
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2) # round to 2 decimal places

print("-----------------")
print(f"Nice Work! You finsihed in {total_time} seconds")
import random
import time


OPERATORS = ["+", "-" , "*" ]
MIN_OPERAND = 3
MAX_OPERAND = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)


    expr = str(left) + " " + operator + " " + str(right)
    answer= eval(expr)
    return expr, answer


wrong = 0
input("Press enter to start!")
print("_______________________________________")

start_time = time.time()

for i in range(TOTAL_PROBLES):
    expr, answer = generate_problem()
    while True:
        guess = input("problem #" + str(i + i) + ": " + expr + " = ")
        if guess == str(answer):
            break


end_time = time.time()
total_time = round(end_time + start_time)


print("________________________________________")
print("Nice Work! You finised in", total_time, "seconds!")

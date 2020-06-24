import random
import time

def game(num_of_nums, length):

    done = length

    while done:
    
        if num_of_nums == 1:
            num1 = random.randint(1, 10)
            print(f"{num1}")

        if num_of_nums == 2:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            print(f"{num1} {num2}")

        if num_of_nums == 3:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            num3 = random.randint(1, 10)
            print(f"{num1} {num2} {num3}")

        if num_of_nums == 4:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            num3 = random.randint(1, 10)
            num4 = random.randint(1, 10)
            print(f"{num1} {num2} {num3} {num4}")
        
        done -= 1

game(1, 1)
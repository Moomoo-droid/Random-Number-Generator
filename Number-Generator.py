import random
import time

def game(num_of_nums, length, min_num, max_num):

    done = length

    while done:
    
        if num_of_nums == 1:
            num1 = random.randint(min_num, max_num)
            print(f"{num1} \n-----")

        if num_of_nums == 2:
            num1 = random.randint(min_num, max_num)
            num2 = random.randint(min_num, max_num)
            print(f"{num1} {num2} \n-----")

        if num_of_nums == 3:
            num1 = random.randint(min_num, max_num)
            num2 = random.randint(min_num, max_num)
            num3 = random.randint(min_num, max_num)
            print(f"{num1} {num2} {num3} \n-----")

        if num_of_nums == 4:
            num1 = random.randint(min_num, max_num)
            num2 = random.randint(min_num, max_num)
            num3 = random.randint(min_num, max_num)
            num4 = random.randint(min_num, max_num)
            print(f"{num1} {num2} {num3} {num4} \n-----")
        
        time.sleep(0.3)
        done -= 1

game(1, 10, 1, 12)
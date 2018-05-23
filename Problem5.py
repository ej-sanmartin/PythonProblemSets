# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# From 1 to 20, removed redundant numbers to make list shorter and speed up runtime
check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    # loops through numbers to be tested
    for num in range(step, 999999999, step):
        # loops thru check_list
        if all(num % n == 0 for n in check_list):
            return num
    return None

print(find_solution(20))

# Answer: 232792560

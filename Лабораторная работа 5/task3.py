import random

def get_unique_list_numbers() -> list[int]:
    num_min = -10
    num_max = 10
    list_ = []
    while len(list_) < 15:
        num = random.randint(num_min, num_max)
        if num not in list_:
            list_.append(num)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

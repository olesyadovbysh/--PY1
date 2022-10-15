list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
index_max = 0
max_ = list_numbers[index_max] # пусть максимальный индекс у первого элемента

for pos, value in enumerate(list_numbers):
    if value > max_: # сравниваем элементы списка с максимальным индексом и присваиваем новое значение
        max_ = value
        index_max = pos
list_numbers[index_max], list_numbers[-1] = list_numbers[-1], list_numbers[index_max]
print(list_numbers)


# max_ = max(list_numbers)
# index_max = list_numbers.index(max_)
# list_numbers[index_max], list_numbers[-1] = list_numbers[-1], list_numbers[index_max]
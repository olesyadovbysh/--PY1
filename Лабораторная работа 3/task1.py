src = not False and True or False and not True

# TODO расписать упрощение выражения

result = True and True or False and False  # not False = True
result = True or False # True and True = True
result = True
print(src == result)

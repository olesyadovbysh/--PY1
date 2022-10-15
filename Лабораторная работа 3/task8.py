money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
current_spend = spend # текущие расходы
total = money_capital + salary

while total > 0:
    total = total - current_spend
    current_spend = current_spend * (increase + 1)
    if total > 0: #тк на этом моменте деньги уже могут закончится
        total = total + salary
        month += 1
print(month)
#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
list = [random.randint(-10, 10) for _ in range(21)]
print(list)
number1 = int(input("введите первое число: "))
number2 = int(input("введите второе число: "))

for i in range(len(list)):
    if number1 <= list[i] <= number2:
        print(i)

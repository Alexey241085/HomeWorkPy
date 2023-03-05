import random

n = int(input("Введите длину списка: "))
random_numbers = [random.randint(1,100) for _ in range(n)]

print(random_numbers)

num1 = int(input("Введите число, которое нужно найти: "))
count1 = 0
result = 0
min = max(random_numbers) - num1

def count():
    count1 = 0
    for i in range(len(random_numbers)):
        if random_numbers[i] == num1:
            count1 += 1
    print(f"Число {num1} встречается {count1} раз(а)")
       
   

count()     
        
for i in random_numbers:
    if abs(i - num1) < min:
        min = abs(i - num1)
        result = i
print(f"Близкое по значению введеного числа {num1}, является {result}")






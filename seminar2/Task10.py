import random

n = int(input("Введите количество монеток: "))


random_coin = [random.randint(0, 1) for _ in range(n)] # 0 -  решка, 1 - орел
print(random_coin)

count = int(0)
count1 = int(0)
for i in random_coin:
    if i > 0:
        count = count + 1
    else:
        count1 = count1 + 1


if count > count1:
    print(f"Количество монет, которые нужно перевернуть {count1}")
else:
    print(f"Количество монет, которые нужно перевернуть {count}")
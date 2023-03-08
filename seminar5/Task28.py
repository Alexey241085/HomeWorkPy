
def sum(a, b):
    if (b == 0):
        return a
    return sum(a + 1, b - 1)


print("Введите первое число; ")
num1 = int(input())
print("Введите второе число; ")
num2 = int(input())
print(f"Сумма чисел ровна {sum(num1, num2)}")

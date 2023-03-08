
def pow(a, b):
    if (b == 1):
        return a
    return a * pow(a, b - 1)


print("Введите первое число; ")
num1 = int(input())
print("Введите второе число; ")
num2 = int(input())
print(pow(num1, num2))

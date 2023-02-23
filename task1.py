a = input ("Введите любое трехзначное число: ")
a = int(a)

b = a%10
a = int(a/10)

c = a%10
a = int(a/10)

print(a+b+c)


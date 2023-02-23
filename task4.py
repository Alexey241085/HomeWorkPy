n = int(input("Введите первое число: "))

m = int(input("Введите второе число число: "))

k = int(input("Сколько долек отломить? :"))



if (k%n == 0 or k%m == 0) and k<n*m:
    print('Yes')
else: 
    print('No')



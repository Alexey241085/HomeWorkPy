a = input("Введите шестизначное число: ")
a = str(a)

b = int(a[0])
c = int(a[1])
d = int(a[2])

n = int(a[3])
m = int(a[4])
k = int(a[5])

sum1 = b + c + d
sum2 = n + m + k

if sum1 == sum2:
   print("YES")
else:
   print("NO")




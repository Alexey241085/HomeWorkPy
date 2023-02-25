
s, p = (int(input()) for _ in '12')
for x in range(1, 1001):
    y = s -x
    if x <= y and x * y == p:
        print(x, y)
       

import math


plane = input("Введите число самолетиков, сделнных Петей, Сережей и Катей: ")
plane = int (plane)

piter = int(plane/6)
serge = int(piter)

katy = (piter+serge)*2 

if plane%6 == 0:
   print(piter,katy,serge)

else: 
   print("Походу Катя врушка?!")



#katy = int(plane/1.5) 

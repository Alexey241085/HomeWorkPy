string = input ("Enter a string: ")
dictionary = {}

for i in string:
    dictionary[i] = dictionary.get(i, 0) + 1


    if dictionary[i] == 1:
        print(i, end= ",") 
    else:
        print(f"{i}_{dictionary[i] - 1}", end=",")
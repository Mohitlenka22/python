l1=[];t1=[]
try:
    for i in range(int(input("Enter size of l1:"))):
        x = int(input("Enter integer: ") )
        if x > 10:
            raise ValueError
        l1.append(x)
except ValueError:
    print("enter only numbers smaller than 10.")
for j in range(int(input("Enter size of t1:"))):
    x = input("Enter string: ")
    t1.append(x)
t1 = tuple(t1)
try:
    index = int(input("Enter index to searched in l1: "))
    if index >= len(l1):
        raise IndexError
    print(l1[index])
except IndexError:
    print("Index out of range.")
try:
     i1 = int(input("Enter index in l1: "))
     i2 = int(input("Enter index in t1: "))
     if l1[i1] + t1[i2]:
        raise TypeError
except TypeError:
    print("Cant concatenate integer with string.")







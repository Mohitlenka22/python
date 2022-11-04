try:
    l1 = list(map(int,input("Enter 3 integers: ").split()))
    t1 = tuple(map(str,input("Enter 3 strings: ").split()))
    try:
        print(f'value at index 4 in l1 : {l1[4]}')
    except IndexError as e:
        print(e)
    try:
        print(f'tuple t2 : {t2}')
    except NameError as e:
        print(e)
    try:
        print(f'concatenation of l1,t1 :{l1 + t1}')
    except TypeError as e:
        print(e)
    try:
        print(f'answer of l1[0]/l2[1]: {l1[0] / l1[1]}')
    except ZeroDivisionError as e:
        print(e)
except ValueError:
    print("Enter correct input.")





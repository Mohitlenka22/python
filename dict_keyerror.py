class No_Key(Exception):
    pass
try:
    d = {'m1':100,'m2':95,'physics':95,'chem':96}
    key = input("Enter key: ")
    if key not in d:
        raise No_Key
    print(f'value is {d[key]}.')
except No_Key:
    print("Key_Error: Key doesnot exist.")



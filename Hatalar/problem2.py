def cift(i):
    if(i%2 != 0):
        raise ValueError
    else:
        return i

liste = [1,2,3,4,5,6,7,89,10,52,6,3,98,8]
for eleman in liste:
    try:
        print(cift(eleman))
    except ValueError:
        pass

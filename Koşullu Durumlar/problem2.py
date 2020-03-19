a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if(a > b and a > c):
    print("{} en büyük sayidir.".format(a))
elif(b > a and b > c):
    print("{} en büyük sayidir.".format(b))
elif(c > a and c > b):
    print("{} en büyük sayidir.".format(c))

import math
#help(math)

print("""****************************

Gelismis Hesap Makinesine Hos Geldiniz...

1.x+y                 8.e**(x)
2.x-y                 9.|x,y|
3./                   10.x!
4.x*y                 11.mod(x,y)
5.log(x)              12.log10(x)
6.log2(x)             13.x**y
7.x**(1/2)            14.1/x


Cikis yapmak icin 'q' ya basiniz.

****************************""")


while True:
    secim = input("Islem seciniz: ")

    if(secim == "q"):
        print("Cikis yapiliyor...")
        break
    elif(secim == "1"):
        x = float(input("x: "))
        y = float(input("y: "))
        print(x+y)

    elif(secim == "2"):

        x = float(input("x: "))
        y = float(input("y: "))
        print(x-y)

    elif(secim == "3"):
        x = float(input("x: "))
        y = float(input("y: "))
        print(x/y)

    elif(secim == "4"):
        x = float(input("x: "))
        y = float(input("y: "))
        print(x*y)

    elif(secim == "5"):
        x = float(input("x: "))
        print(math.log(x))


    elif(secim == "6"):
        x = float(input("x: "))
        print(math.log2(x))



    elif(secim == "7"):
        x = float(input("x: "))
        print(math.sqrt(x))



    elif(secim == "8"):
        x = float(input("x: "))
        print(math.exp(x))

    elif(secim == "9"):
        x = float(input("x: "))
        print(math.fabs(x))

    elif(secim == "10"):
        x = float(input("x: "))
        print(math.factorial(x))

    elif(secim == "11"):
        x = float(input("x: "))
        y = float(input("y: "))
        print(x%y)

    elif(secim == "12"):
        x = float(input("x: "))
        print(math.log10(x))

    elif(secim == "13"):
        x = float(input("x: "))
        y = float(input("y: "))
        print(math.pow(x,y))

    elif(secim == "14"):
        x = float(input("x: "))
        if(x == 0):
            print("Gecersiz islem...")
        else:
            print(1/x)

    else:
        print("Gecersiz islem")

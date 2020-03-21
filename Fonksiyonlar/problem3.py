#Kullanıcıdan 2 tane sayı alarak bu sayıların
#en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

def EKOK(sayi1,sayi2):
    ekk = 1
    i = 2
    while True:
        if(sayi1 % i == 0 and sayi2 % i == 0): #İki sayıda i ye bolunuyorsa.
            ekk  = ekk*i

            sayi1 = sayi1 // i
            sayi2 = sayi2 // i

        elif(sayi1 % i == 0 and sayi2 %i != 0):
            ekk  = ekk*i

            sayi1 = sayi1 // i

        elif(sayi1 % i != 0 and sayi2 %i == 0):
            ekk  = ekk*i

            sayi2 = sayi2 // i
        else:
            i += 1
        if(sayi1 == 1 and sayi2 == 1):
            break
    return ekk


sayi1 = int(input("sayi 1: "))
sayi2 = int(input("sayi 2: "))

print(EKOK(sayi1,sayi2))

#Kullanıcıdan 2 tane sayı alarak bu sayıların
#en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
def EBOB(sayi1,sayi2):
    #ortak_bolenler = []
    en_buyuk_bolen = 0
    for i in range(1,int(sayi1/2)+1):
        if(sayi1 % i == 0):
            for j in range(i,int(sayi2/2)+1):
                if(sayi2 % j == 0):
                    if(i == j):
                        #ortak_bolenler.append(j)
                        if(j > en_buyuk_bolen):
                            en_buyuk_bolen = j

    return en_buyuk_bolen

#print(EBOB(39,26))


sayi1 = int(input("Sayi 1: "))
sayi2 = int(input("Sayi 2: "))

print(EBOB(sayi1,sayi2))

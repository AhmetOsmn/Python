#Armstrong sayisi mi?
#def basamak_sayisi(x):

def armstrong(x): #sx sayisinin rakamlarının basamak sayısı kadar üssünü alır ve bu sayıların toplamlarını döndürür.
    toplamlari = 0
    for eleman in rkm(x):
        toplamlari += eleman ** bs(x)
    return toplamlari

def rkm(x): #x sayisinin rakamlarını ayırarak bir listeye atar ve bu listeyi döndürür.
    liste = []
    while(x > 0):
        a = x-(x//10)*10
        liste.append(a)
        x //= 10 #156 -> 15 ->1
        #print(x)
    return liste #print(l)

def bs(x): #x sayisinin basamak sayisini döndüren fonksiyon.
    bs = 0
    while(x > 0):
        x //= 10
        bs += 1

    return bs

sayi = int(input("Sorgulamak istediginiz sayi: "))
sayi_bs = bs(sayi)
rakamlari = rkm(sayi)

#print(sayi_bs)
#print(rakamlari)

if(sayi == armstrong(sayi)): # eğer sayi;kendisini oluşturan rakamlarının,kendisnin basmak sayisi kadar üslerinin toplamına eşitse armstrong sayıdır..
    print("Sayiniz Armstrong bir sayidir")
else:
    print("Sayiniz Armstrong değildir")

"""
Udemy cözümü:

    sayı = input("Sayı:")
    basamak_sayisi = len(sayı)
    sayı = int(sayı)
    basamak = 0
    toplam = 0

    gecici_sayı = sayı

    while (gecici_sayı > 0):

        basamak = gecici_sayı % 10

        toplam += basamak ** basamak_sayisi

        gecici_sayı //= 10


    if (toplam == sayı):
        print(sayı,"bir armstrong sayısıdır.")
    else:
        print(sayı,"bir armstrong sayısı değildir.")

"""

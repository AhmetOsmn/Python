#Mükemmel sayi mi?
#Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

a = int(input("Sorgulamak istediginiz sayi: "))

bolenler = []

for i in range(1,int(a/2)+1):
    if(a%i == 0):
        bolenler.append(i)

#print(bolenler)
bolen_toplam = 0
for eleman in bolenler:
    bolen_toplam += eleman
#print(bolen_toplam)
if(bolen_toplam == a):
    print("Girdiginiz sayi mukemmel sayidir...")
else:
    print("Girdiginiz sayi mukemmel sayi degildir...")


"""
Udemy cözümü:
    sayı = int(input("Sayı:"))

    i = 1
    toplam = 0
    while (i < sayı):
        if (sayı % i == 0):
            toplam += i
        i += 1

    if (toplam == sayı):
        print(sayı,"mükemmel bir sayıdır.")
    else:
        print(sayı,"mükemmel bir sayı değildir.")

"""

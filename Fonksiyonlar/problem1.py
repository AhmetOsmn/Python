#Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
#Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
def mukemmel():
    for i in range(1,1001):
        toplam = 0
        #liste = []
        for j in range(1,int(i/2)+1): #her i için i nin bölenlerini tarıyorum.
            if (i % j == 0):
                #liste.append(j)
                toplam += j
        #print(liste)
        #print(i,toplam)
        if(toplam == i):
            print(i,"Mükemmel sayidir")
mukemmel()

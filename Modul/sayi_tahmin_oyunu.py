import random
import time

print("""********************************


Sayi Tahmin Oyunu

1-40 arasındaki sayiyi tahmin edin.


**********************************""")

rastgele_sayi = random.randint(1,40)
tahmin_hakki = 10

while True:
    tahmin = int(input("Tahmininiz: "))

    if(tahmin < rastgele_sayi):
        print("Kiyaslaniyor...")
        time.sleep(1) #program 1 sn duraklatılacak.
        print("Daha yüksek bir sayi giriniz..")
        tahmin_hakki -= 1
    elif(tahmin > rastgele_sayi):
        print("Kiyaslaniyor...")
        time.sleep(1)
        print("Daha küçük sayi giriniz...")
        tahmin_hakki -= 1
    else:
        print("Kiyaslaniyor")
        time.sleep(1)
        print("Tebrikler! Sayimiz: ",rastgele_sayi)
        break
    if(tahmin_hakki == 0):
        print("Tahmin Hakkiniz Bitti...")
        print("Sayimiz: ",rastgele_sayi)
        break

    

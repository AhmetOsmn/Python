#Her bir while döngüsünde kullanıcıdan bir sayı alın ve
#kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.
#Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

toplam = 0
print("Cikis yapmak icin q ya basiniz...")
while True:
    sayi = input("Sayi giriniz: ")
    if(sayi == "q"):
        break
    toplam = toplam + int(sayi)
print(toplam)

"""
Udemy cözüm:
    toplam = 0

    while True:

       sayı = input("Sayı:")

        if (sayı == "q"):
            break
        sayı = int(sayı)

        toplam += sayı

    print("Girdiğiniz Sayıların Toplamı:",toplam)

"""

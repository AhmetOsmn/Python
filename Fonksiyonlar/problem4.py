#Kullanıcıdan 2 basamaklı bir sayı alın ve
#bu sayının okunuşunu bulan bir fonksiyon yazın.

def okunus(sayi):
    bb = ["","bir","iki","uc","dort","bes","altı","yedi","sekiz","dokuz"] #`Basltaki "" kullanmamızın nedeni listelerde indisler 0 dan baslıyor.
                                                                          #Bizim elde ettiğimiz ile ilgili olan indis aynı olmalı.

    ob = ["","on","yirmi","otuz","kirk","elli","altmis","yetmiş","seksen","doksan"]

    onlar = sayi // 10
    birler = sayi % 10


    return ob[onlar] + "\t" +bb[birler]

sayi = int(input("Sayi: "))

print(okunus(sayi))

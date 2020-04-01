# -*- coding: utf-8 -*-
from sarki import *

print("""***********************************
Sarki Programina Hosgeldiniz.

Islemler:

1.Sarkilari goster

2.Sarki sorgula

3.Sarki ekle

4.Sarki sil

5.Toplam sureyi gor

Cikis yapmak icin 'q' ya basin.

***********************************""")


arsiv = Arsiv()


while True:
    islem = input("Islem seciniz: ")

    if(islem == "q"):
        print("Program sonlandiriliyor")
        time.sleep(1)
        break

    elif(islem == "1"):
        arsiv.sarkilari_goster()

    elif(islem == "2"):
        isim = input("Sarki ismi: ")
        print("Sarki sorgulaniyor.")
        time.sleep(2)
        arsiv.sarki_sorgula(isim)

    elif(islem == "3"):
        isim = input("Sarki ismi: ")
        sanatci = input("Sanatci: ")
        album = input("Album: ")
        produksiyon = input("Produksiyon Sirketi: ")
        sure = float(input("Sarki Suresi: "))
        yeni_sarki = Sarki(isim,sanatci,album,produksiyon,sure) #yeni_sarki adinda nesne olusturduk.
        print("Sarki ekleniyor..")
        time.sleep(2)
        arsiv.sarki_ekle(yeni_sarki)
        print("Sarki basariyla eklendi !")

    elif(islem == "4"):
        isim = input("Silinecek sarkinin ismi: ")
        cevap = input("Emin misiniz ? (E/N)")

        if(cevap == "E"):
            print("Sarki siliniyor...")
            time.sleep(2)
            arsiv.sarki_sil(isim)
            print("Sarki basariyla silindi !")

    elif(islem == "5"):
            arsiv.toplam_sure()

# -*- coding: utf-8 -*-
from kutuphane import * #kutuphane'deki classlarimizi kullanabiliriz.

print("""***********************************
Kutuphane Programina Hosgeldiniz.

Islemler:

1.Kitaplari Goster

2.Kitap Sorgulama

3.Yazarin kitaplarini ara

4.Turune gore kitaplari ara

5.Yayin evinin kitaplarini gor

6.Kitap Ekle

7.Kitap Sil

8.Baski Yukselt



Cikis yapmak icin 'q' ya basin.

***********************************""")

kutuphane = Kutuphane()



while True:
    islem = input("Islem seciniz: ")

    if(islem == "q"):
        print("Program sonlandiriliyor")
        time.sleep(1)
        break

    elif(islem == "1"):
        kutuphane.kitaplari_goster()

    elif(islem == "2"):
        isim = input("Kitap ismi: ")
        print("Kitap sorgulaniyor.")
        time.sleep(2)
        kutuphane.kitap_sorgula(isim)

    elif(islem == "3"):
        yazar = input("Yazarin ismi: ")
        print("Kitaplar araniyor...\n")
        print("-------------------------------------------------------")
        time.sleep(1)
        kutuphane.yazar_ismi(yazar)
        print("-------------------------------------------------------")

    elif(islem == "4"):
        tur = input("Turu: ")
        print("Kitaplar araniyor...\n")
        print("-------------------------------------------------------")
        time.sleep(1)
        kutuphane.kitap_turu(tur)
        print("-------------------------------------------------------")

    elif(islem == "5"):
        yayinevi = input("Yayin evinin ismi: ")
        print("Kitaplar araniyor...\n")
        print("-------------------------------------------------------")
        time.sleep(1)
        kutuphane.yayinevi(yayinevi)
        print("-------------------------------------------------------")

    elif(islem == "6"):
        isim = input("Kitap ismi: ")
        yazar = input("Yazari: ")
        yayinevi = input("Kitabin yayin evi: ")
        tur = input("Kitabin turu: ")
        baski = int(input("Baski: "))
        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski) #yeni_kitap adinda nesne olusturduk.
        print("Kitap ekleniyor..")
        time.sleep(2)
        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap basariyla eklendi !")

    elif(islem == "7"):
        isim = input("Silinecek kitabin ismi: ")
        cevap = input("Emin misiniz ? (E/N)")

        if(cevap == "E"):
            print("Kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap basariyla silindi !")

    elif(islem == "8"):
        isim = input("Baskisini yukseltmek istediginiz kitabin ismi: ")
        print("Baski yukseltiliyor...")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Baski basariyla yukseltildi !")

    else:
        print("Geceriz islem")

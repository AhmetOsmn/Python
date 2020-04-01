# -*- coding: utf-8 -*-
#modul olarak kullanacagiz.

import sqlite3
import time

class Kitap():
    def __init__(self,isim,yazar,yayinevi,tur,baski):

        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):
        return "Kitap Ismi: {}\nYazar: {}\nYayin Evi: {}\nTur: {}\nBaski: {}\n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)

class Kutuphane():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self): #veritabanini ve tabloyu olusturur.
        self.baglanti = sqlite3.connect("kutuphane.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT,yazar TEXT,yayinevi TEXT,tur TXT,baski INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitaplari_goster(self):
        sorgu = "SELECT * FROM kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall() #kitaplar liste icinde demet halinde bulunuyorlar.
        if(len(kitaplar) == 0):
            print("Kutuphanede kitap bulunmuyor...")
        else:

            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4]) #i[0]:kitap ismi,i[1]:yazar........
                print(kitap)

    def kitap_sorgula(self,isim):
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,)) #sorguyu calistir.
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar) == 0): #kitap,kitaplar tablosunda yoksa:
            print("Boyle bir kitap bulunmuyor...")
        else: #eger kitap var ise:liste icinde demet olarak bulunacak.
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            #kitap[0] zaten elimizde tek demetten olusan bir liste var,
            #kitap[0][0] elimizdeki demetin ilk elemani yani kitabın ismi,
            #kitap[0][1] yazari
            #       .
            #       .
            #       .
            print(kitap)

    def kitap_ekle(self,kitap): #kitap -> nesne
        sorgu = "INSERT INTO kitaplar VALUES(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
        self.baglanti.commit() #yapmassak veritabanina bilgi gitmeyecek ve guncelleme olmayacak.

    def kitap_sil(self,isim):
        sorgu = "DELETE FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def baski_yukselt(self,isim):
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall() #eger girilen kitap listemde var ise bana bir demet donecek.
        if(len(kitaplar) == 0):
            print("Boyle bir kitap bulunmuyor...")
        else:
            baski = kitaplar[0][4]
            baski += 1

            sorgu2 = "UPDATE kitaplar SET baski = ? WHERE isim = ?"
            self.cursor.execute(sorgu2,(baski,isim))
            self.baglanti.commit()

    def yayinevi(self,yayinevi):
        sorgu = "SELECT * FROM kitaplar WHERE yayinevi = ?"
        self.cursor.execute(sorgu,(yayinevi,))
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Yayin evinin herhangi bir kitabi bulunmuyor...")
        else:
            for i in kitaplar:
                print("Kitap ismi: {}\nYazari: {}\nTuru: {}\nBaski: {}\n".format(i[0],i[1],i[3],i[4]))

    def yazar_ismi(self,yazar_isim):
        sorgu = "SELECT * FROM kitaplar WHERE yazar = ?"
        self.cursor.execute(sorgu,(yazar_isim,))
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Bu isimde yazarin kitabi bulunmuyor...")
        else:
            for i in kitaplar:
                print("Kitap ismi: {}\nYayinevi: {}\nTuru: {}\nBaski: {}\n".format(i[0],i[2],i[3],i[4]))

    def kitap_turu(self,tur):
        sorgu = "SELECT * FROM kitaplar WHERE tur = ?"
        self.cursor.execute(sorgu,(tur,))
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Bu turde bir kitap bulunmuyor...")
        else:
            for i in kitaplar:
                print("Kitap ismi: {}\nYazari: {}\nYayinevi: {}\nBaski: {}\n".format(i[0],i[1],i[2],i[4]))

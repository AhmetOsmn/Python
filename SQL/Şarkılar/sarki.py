# -*- coding: utf-8 -*-
import sqlite3
import time

class Sarki():
    def __init__(self,isim,sanatci,album,produksiyon,sure):
        self.isim = isim
        self.sanatci = sanatci
        self.album = album
        self.produksiyon = produksiyon
        self.sure = sure

    def __str__(self):
        return "Sarki ismi: {}\nSanatci: {}\nAlbum: {}\nProdukyiyon sirketi: {}\nSarki suresi: {}\n".format(self.isim,self.sanatci,self.album,self.produksiyon,self.sure)

class Arsiv():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("arsiv.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS sarkilar (isim TEXT,sanatci TEXT,album TEXT,produksiyon TEXT,sure FLOAT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def sarkilari_goster(self):
        sorgu = "SELECT * FROM sarkilar"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()
        if(len(sarkilar) == 0):
            print("Listede sarki bulunmuyor...")
        else:

            for i in sarkilar:
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)

    def sarki_sorgula(self,isim):
        sorgu = "SELECT FROM sarkilar WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        sarkilar = self.cursor.fetchall()

        if(len(sarkilar) == 0):
            print("Boyle bir sarki bulunmuyor...")
        else:
            for i in sarkilar:
                sarki = Sarki(sarkilar[0][0],sarkilar[0][1],sarkilar[0][2],sarkilar[0][3],sarkilar[0][4])
                print(sarki)

    def sarki_ekle(self,sarki):
        sorgu = "INSERT INTO sarkilar VALUES (?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatci,sarki.album,sarki.produksiyon,sarki.sure))
        self.baglanti.commit()

    def sarki_sil(self,isim):
        sorgu = "DELETE FROM sarkilar WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def toplam_sure(self):
        sorgu = "SELECT * FROM sarkilar"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()
        toplam_sure = 0

        for i in sarkilar:
            sure = i[4]
            toplam_sure += sure

        print("Sarkilarin toplam suresi: {}".format(toplam_sure))

import sqlite3


#connection = con' degisken.
#kütüphane.db'veritabaninin adi.
con = sqlite3.connect("kütüphane.db")
#cursur = imlec
cursor = con.cursor()
def tablo_olustur():
    #CREATE TABLE IF NOT EXISTS -> sorgu
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (isim TEXT,Yazar TEXT,Yayin_evi TEXT,Sayfa_Sayisi INT)")
    con.commit() #eger yapmazsak sorgu calismayacak ve Tablo olusmayacak.
"""
Database baglanma bu kadar.
"""
def veri_ekle():
    #"Insert into kitaplik Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)" -> sorgu
    cursor.execute("Insert into kitaplik Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

def veri_eklee(isim,yazar,yayinevi,sayfa):
    #Insert into kitaplik Values(?,?,?,?)",(isim,yazar,yayinevi,sayfa) -> sorgu
    cursor.execute("Insert into kitaplik Values(?,?,?,?)",(isim,yazar,yayinevi,sayfa))
    #(?,?,?,?)",(isim,yazar,yayinevi,sayfa) yapisi -> "{} asd".format(a) yapisi gibi calisir.
    con.commit()

#tablo_olustur()
#veri_ekle()

isim = input("Isim: ")
yazar = input("Yazar: ")
yayinevi = input("Yayin evi: ")
sayfa = int(input("Sayfa: "))

veri_eklee(isim,yazar,yayinevi,sayfa) #normal fonksiyon kullanimi.

con.close() #dosya kapatmak gibi.

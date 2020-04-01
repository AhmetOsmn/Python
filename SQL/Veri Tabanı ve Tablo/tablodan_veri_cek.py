#Select*Fram kitaplik -> kitaplik tablosundan bütün bilgileri almamaizi saglar.
#Select isim,yazar From kitaplik -> Tablodan sadece isim ve yazar ozelliklerini almamizi saglar.
#Select*From kitaplik where Yayıinevi = 'Everest' -> yayin evi sadece Everest olan kitalari cek.
import sqlite3
con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()
def verileri_al():
    cursor.execute("SELECT * FROM kitaplik") #SELECT * FROM kitaplik sorgusu -> Butun verileri aldik.
    liste = cursor.fetchall() #cursor uzerindeki butun bilgileri liste olarak dondurecek.
    print("Kitaplik tablosunun bilgileri...")

    for i in liste:
        print(i) #Her satir bir kitabi simgeliyor.

def isim_yazar_al():
    cursor.execute("SELECT isim,Yazar FROM kitaplik")
    liste = cursor.fetchall()

    for i in liste:
        print(i)

def yayinevi_al(Yayinevi):
    cursor.execute("SELECT * FROM kitaplik where Yayin_evi = ?",(Yayinevi,))
    #SELECT * FROM kitaplik where Yayin_evi sorgusu -> Yayin_evi sutunundan al demek.
    liste = cursor.fetchall()

    for i in liste:
        print(i)

#verileri_al()
#isim_yazar_al()
#yayinevi_al("Everest")

con.close()

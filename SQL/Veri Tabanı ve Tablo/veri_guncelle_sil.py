import sqlite3

con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()

def verileri_al():
    cursor.execute("SELECT * FROM kitaplik")
    liste = cursor.fetchall()

    for i in liste:
        print(i)

def veri_guncelle(eski_yayinevi,yeni_yayinevi):
    cursor.execute("UPDATE kitaplik SET Yayin_evi = ? where Yayin_Evi = ?",(yeni_yayinevi,eski_yayinevi))
                                                  #yeni---------------eski
    con.commit() #con.commit() veritabanini guncellerken,ekleme,cikartma yaparken kullanilir.

def veri_sil(yazar):
    cursor.execute("DELETE FROM kitaplik where Yazar = ?",(yazar, )) #Yazari 'yazar' degiskeni olan butun kayitlar silinecek.
    con.commit()


#verileri_al()
#veri_guncelle("Everest","Doğan") #Tablodaki butun "Everest" yayin evleri "Doğan" ile degisitrildi.
#verileri_al()
veri_sil("Ahmet Ümit") #Yazarinin "Ahmet Ümit" oldugu butun kayitlar silinecek.
verileri_al()

con.close()

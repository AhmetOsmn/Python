
class Araba():
    model = "Renault Megane"
    renk = "Gumus"
    b_gucu = 110
    silindir = 4

    def __init__(self): #self = objeyi olusturdugumuzda otomatik olarak objemizi gösteren referanstır.
        print("init fonksiyonu cagirildi..")







araba1 = Araba() # init fonksiyonu cagirildi.
#print(araba1)

#araba2 = Araba()
#print(araba2)

print(araba1.model) #araba1 objesinin özelliklerine . ile erişiyoruz.
print(araba1.renk)
print(araba1.b_gucu)
print(araba1.silindir)

#print(Araba.model)

#print(dir(araba1)) #pythonun otamatik olarak tanımladıgı fonksiyonlar vardır.
#init = constructor

class Araba():

    def __init__(self,model = "Bilgi yok",renk = "Bilgi yok",b_gucu = 70,silindir = 4): #varsayılan olarak tanımlama şekli.
       print("init fonksiyonu cagirildi.")
       self.model = model
       self.renk = renk
       self.b_gucu = b_gucu
       self.silindir = silindir

#araba3 = Araba("Renault","Kirmizi",110,4)
#araba4 = Araba("Pegout","Beyaz",110,4)

#print(araba3.model)
#print(araba4.model)

araba5 = Araba(renk = "Siyah")
print(araba5.renk)
print(araba5.model)

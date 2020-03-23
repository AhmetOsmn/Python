class Hayvan():
    def __init__(self,ayak = 0,kuyruk = "Bilgi yok",goz = "Var"):
        print("Hayvan init fonksiyonu")
        self.ayak = ayak
        self.kuyruk = kuyruk
        self.goz = goz

    def yürümek(self):
        print("Yürürler.")

    def beslenmek(self):
        print("Yemek yerler.")

    def üremek(self):
        print("Urerler.")

    def soluk(self):
        print("Nefes alirlar")

class Kopek(Hayvan):
    def __init__(self,ayak,kuyruk,goz,tuy):
        super().__init__(ayak,kuyruk,goz)
        self.tuy = tuy

    def soluk(self):
        super().soluk()

    def kosmak(self):
        print("Koşabilirler")

class Kus(Hayvan):
    def __init__(self,ayak,kuyruk,goz,tuy,gaga):
        super().__init__(ayak,kuyruk,goz)
        self.tuy = tuy
        self.gaga = gaga

    def ucmak(self):
        print("ucabilirler")

class At(Hayvan):
    def __init__(self,ayak,kuyruk,goz):
        super().__init__(ayak,kuyruk,goz)

    def hizli_kosmak(self):
        print("Cok hizli kosabilirler")


hayvan = Hayvan()
hayvan.beslenmek()
hayvan.üremek()

kopek = Kopek(4,"var",2,"var")
kus = Kus(2,"Var",2,"var","var")
at = At(4,"Var",2)

kopek.soluk()
kopek.kosmak()

kus.ucmak()
at.hizli_kosmak()

import time

class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller = [],hobiler = []):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller
        self.hobiler = hobiler

    def zam_yap(self,zam_miktari): #metodlarda self parametresini göndermek zorundayız çünkü objenin referansı olarak kullanılıyor..
        print("Zam yapiliyor....")
        time.sleep(1)
        self.maas += zam_miktari

    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor...")
        time.sleep(1)
        self.diller.append(yeni_dil)

    def hobi_ekle(self,yeni_hobi):
        print("Hobi ekleniyor...")
        time.sleep(1)
        self.hobiler.append(yeni_hobi)




    def bilgileri_goster(self):
        print("""

        Yazilimci Objesinin Ozellikleri

        Isim: {}

        Soyisim: {}

        Numara: {}

        Maas: {}

        Bildigi Diller: {}

        Hobileri: {}
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller,self.hobiler))

yazilimci = Yazilimci("Ahmet","Sezgin",5312541276,4000,["Python","Java","C"],)

#yazilimci.bilgileri_goster()

yazilimci.dil_ekle("Flutter")
yazilimci.bilgileri_goster()

yazilimci.zam_yap(500)
yazilimci.bilgileri_goster()

yazilimci.hobi_ekle("Basketbol Oynamak")
yazilimci.bilgileri_goster()

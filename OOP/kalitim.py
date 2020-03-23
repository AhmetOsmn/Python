#Inheritance
class Calisan():
    def __init__(self,isim,maas,departman):
        print("Calisan sinifinin __init__ fonksiyonu..")

        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Casian sinifinin bilgileri...")
        print("İsim: {}\nMaas: {}\nDepartman: {}\n".format(self.isim,self.maas,self.departman))

    def departman_degis(self,yeni_departman):
        self.departman = yeni_departman

class Yonetici(Calisan): #Calisan sinifindan kaliitm ile butun metodları,ozellikleri miras aldirmis olduk.
    #pass #eger classı sonradan tanımlamak istiyorsak pass kullanabiliriz.

    def __init__(self,isim,maas,departman,kisi_sayisi): #Override etmis olduk.3 Parametre ayni fakat,
                                                        #yeni eklemek istedigimiz bir ozellik oldugunda tekrar yazmak zorundayiz.

        print("Yonetici sinifinin __init__ fonksiyonu..")
        super().__init__(isim,maas,departman)
        """
                                              # Calisan sinifindaki yaptıgım isin aynisini tekrar yapmamak icin,
        self.isim = isim                      # super().__init__(isim,maas,departman) ifadesini kullanarak daha pratik yaptım.
        self.maas = maas                      # Yeni eklemek istedigim ifadeyi ise manuel olarak; self.kisi_sayisi = kisi_sayisi
        self.departman = departman            # olarak girdim.

        """
        self.kisi_sayisi = kisi_sayisi

    def bilgileri_goster(self): #bilgileri_goster fonksiyonu override edilmis oldu.
        print("Yonetici sinifinin bilgileri...")
        print("İsim: {}\nMaas: {}\nDepartman: {}\nKisi Sayisi: {}\n".format(self.isim,self.maas,self.departman,self.kisi_sayisi))
                                                                                                              #override(kisi_sayisi)

    def zam_yap(self,zam_miktari): #Yonetici sinifina ekstra olarak istedigimiz gibi metod yazabiliriz.
        self.maas += zam_miktari

#yonetici = Yonetici("Ahmet",4000,"IT")
"""
yonetici.bilgileri_goster()
yonetici.departman_degis("Insan kaynaklari")
yonetici.bilgileri_goster()

#print(dir(yonetici)) #miras aldigimizi gorebiliriz.

yonetici.bilgileri_goster()
yonetici.zam_yap(1000)
yonetici.bilgileri_goster()
"""
yonetici1 = Yonetici("Osman",5000,"Bilisim",20)
yonetici1.bilgileri_goster()

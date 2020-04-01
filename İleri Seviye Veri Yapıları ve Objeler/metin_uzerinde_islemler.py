class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_icerigi = file.read()
            #print(dosya_icerigi)
            kelimeler = dosya_icerigi.split() #split() bos birakirsak bosluga gore ayiri.
            """
            for i in kelimeler:
                print(i)
            """
            self.sade_kelimeler = list() #self yazmamizin nedeni baska yerlerde de kullanabilmek.
            for i in kelimeler:
#strip(x) fonksiyonu:stringin basinda ve sonunda bulunan x degerlerini siliyor.
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                self.sade_kelimeler.append(i)

            #print(self.sade_kelimeler)
            """
            for i in self.sade_kelimeler:
                print(i)
            """
    def tum_kelimeler(self):

        kelimeler_kumesi = set() #her kelimeden 1 adet olmasi icin kumeye atiyoruz.
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)
        print("Tum kelimeler...")
        for i in kelimeler_kumesi:
            print(i)
            print("*********************************")


    def kelime_frekansi(self):
        self.kelime_sozluk = dict()
        for i in self.sade_kelimeler:
            if(i in self.kelime_sozluk): #sozlukte kelime var ise degerini 1 arttir.
                self.kelime_sozluk[i] +=1
            else:
                self.kelime_sozluk[i] = 1
        """
        for kelime,sayi in self.kelime_sozluk.items():
            print("{}' kelimesi {} defa geciyor..".format(kelime,sayi))
            print("-----------------------------------------")
        """
        return self.kelime_sozluk

#kullanicidan kelime al,kelime var ise kac kere kullanildigini dondur.Eger yok ise 'Kelime metinde yok' yazdir.
    def kelime_al(self):
        kelime = input("Kelime: ")
        dosya.kelime_frekansi()
        if(kelime in self.kelime_sozluk):
            print("{}'kelimesi metinde {}'defa geciyor.".format(kelime,self.kelime_sozluk[kelime]))
        else:
            print("{} kelimesi metinde bulunmuyor.")



dosya = Dosya()
#dosya.tum_kelimeler()
#dosya.kelime_frekansi()
dosya.kelime_al()

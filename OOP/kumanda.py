import time
import random

class Kumanda():

    def __init__(self,tv_durum = "Kapali",tv_ses = 0,kanal_listesi = ["Trt"],kanal = "Trt"):

        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def kanal_ileri(self):
        if(self.kanal_listesi.index(self.kanal) < len(self.kanal_listesi)-1):
            self.kanal = self.kanal_listesi[self.kanal_listesi.index(self.kanal)+1]
            print("Kanal: ",self.kanal)
        else:
            print("Son kanal..")
    def kanal_geri(self):
        if(self.kanal_listesi.index(self.kanal) > 0):
            self.kanal = self.kanal_listesi[self.kanal_listesi.index(self.kanal)-1]
            print("Kanal: ",self.kanal)
        else:
            print("İlk kanal")

    def tv_ac(self):
        if(self.tv_durum == "Acik"):
            print("Televizyon zaten acik...")
        else:
            print("Televizyon aciliyor...")
            self.tv_durum = "Acik"


    def tv_kapat(self):
        if(self.tv_durum == "Kapali"):
            print("Televizyon zaten kapali...")
        else:
            print("Televizyon kapatiliyor...")
            self.tv_durum = "Kapali"

    def ses_ayarlari(self):
        while True:
            cevap = input("Ses azalt: '<' \nSesi arttir: '>'\nCikis: 'cikis'\n")

            if(cevap == "<"):
                if(self.tv_ses != 0 and self.tv_ses > 0):
                    self.tv_ses -= 5
                    print("Ses: ",self.tv_ses)

            elif(cevap == ">"):
                if(self.tv_ses != 100 and self.tv_ses < 100):
                    self.tv_ses += 5
                    print("Ses: ",self.tv_ses)

            else:
                print("Ses guncellendi: ",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi...")

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Su anki kanal: ",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "\nTv durumu: {}\nTv ses: {}\nKanal listesi: {}\nSu anki kanal {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda = Kumanda()
print("""

      Televizyon uygulamasi

1.Tv ac

2.Tv kapat

3.Ses ayarlari

4.Kanal ileri

5.Kanal geri

6.Kanal ekle

7.Kanal sayisini ogren

8.Rastgele kanala gecme

9.Televizyon bilgileri

Cikis icin 'q' ya basın.

""")

while True:
    islem = input("İslemi giriniz: ")

    if(islem == "q"):
        print("Cikis yapiliyor")
        break

    elif(islem == "1"):
        kumanda.tv_ac()

    elif(islem == "2"):
        kumanda.tv_kapat()

    elif(islem == "3"):
        kumanda.ses_ayarlari()

    elif(islem == "4"):
        kumanda.kanal_ileri()

    elif(islem == "5"):
        kumanda.kanal_geri()

    elif(islem == "6"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayirarak girin: ")
        kanal_listesi = kanal_isimleri.split(",") # ',' e gore ayir.

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif(islem == "7"):
        print("Kanal sayisi: ",len(kumanda))

    elif(islem == "8"):
        kumanda.rastgele_kanal()

    elif(islem == "9"):
        print(kumanda)
    else:
        print("Gecersiz islem...")

import time

class Bilgisayar():
    def __init__(self,marka = "Bilgi yok",ram = 0,ekran = 0,islemci = "Bilgi yok",hafiza = 0):
        self.marka = marka
        self.ram = ram
        self.ekran = ekran
        self.islemci = islemci
        self.hafiza = hafiza

    def __str__(self):
        return "Marka: {}\nRam(gb): {}\nEkran(inch): {}\nİslemi: {}\nHafiza(tb): {}".format(self.marka,self.ram,self.ekran,self.islemci,self.hafiza)

    def __len__(self):
        return self.ekran

    def marka_degistir(self,yeni_marka):
        print("Marka degistiriliyor...")
        time.sleep(0.5)
        self.marka = yeni_marka


    def ram_degistir(self,yeni_ram):
        print("Ram degistiriliyor...")
        time.sleep(0.5)
        self.ram = yeni_ram

    def ekran_degistir(self,yeni_ekran):
        print("Ekran degistiriliyor...")
        time.sleep(0.5)
        self.ekran = yeni_ekran

    def islemci_degistir(self,yeni_islemci):
        print("İslemci degistiriliyor...")
        time.sleep(0.5)
        self.islemci = yeni_islemci

    def hafiza_degistir(self,yeni_hafiza):
        print("Hafiza degistiriliyor...")
        time.sleep(0.5)
        self.hafiza = yeni_hafiza



bilgisayar = Bilgisayar()
#print(bilgisayar)
#print(len(bilgisayar))

print("""
      Bilgisayar özellik degisim ekrani

1.Güncel özellikleri gör.

2.Markasini degistir.

3.Ramini degistir.

4.Ekran boyutunu degistir.

5.Islemcisini degistir.

6.Hafizasini degistir.

Cikis yapmak icin '0' a basiniz.

""")

while True:
    islem = input("Islem seciniz: ")

    if(islem == "0"):
        print("Cikiliyor..")
        break

    elif(islem == "1"):
        print(bilgisayar)

    elif(islem == "2"):
        yeni_marka = input("Marka: ")
        bilgisayar.marka_degistir(yeni_marka)

    elif(islem == "3"):
        yeni_ram = int(input("Ram: "))
        bilgisayar.ram_degistir(yeni_ram)

    elif(islem == "4"):
        yeni_ekran = float(input("Ekran (inch): "))
        bilgisayar.ekran_degistir(yeni_ekran)

    elif(islem == "5"):
        yeni_islemci =input("Islemci: ")
        bilgisayar.islemci_degistir(yeni_islemci)

    elif(islem == "6"):
        yeni_hafiza = float(input("Hafiza(TB): "))
        bilgisayar.hafiza_degistir(yeni_hafiza)

    else:
        print("Gecersiz islem")

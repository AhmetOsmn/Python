# -*- coding: utf-8 -*-
"""
"şiir.txt" şeklinde bir dosya oluşturun ve içinde şu satırlar yer alsın.

                    Memlekete sis çökmüş bir gece
                    Usulca yanağıma sen düşüyorsun
                    Sabah saat dokuzu beş geçe
                    Terk edip bizleri gidiyorsun
                    Ayrılık bu kadar yakmamıştı içimizi
                    Farkında mısın bilmiyorum
                    Aldın beraberinde cumhuriyetimizi
                    Korkunç bir veda, sararmıştı her yer
                    Ellerini uzat tutmak istiyoruz
                    Masmavi gözleri kaybetmiş çocuk
                    Aldı bir sabah ruhumuzu
                    Lakin nasıl bölmesin yokluğun uykumuzu

Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın.
"""
from functools import reduce
class Dosya():
    def __init__(self):
        with open("problem2_şiir.txt","r",encoding="utf-8") as file:
            self.siir_icerik = file.readlines()
            #print(self.siir_icerik)
            self.akrostis = list()

            for i in self.siir_icerik:
                self.satir_kelimeleri = i.split()
                #print(self.satir_kelimeleri)

                for j in self.satir_kelimeleri:
                    self.ilk_kelime = j.split(",")
                    #print(self.ilk_kelime)

                    for k in self.ilk_kelime:
                        #print(k)

                        for z in k:
                            #print(z)
                            self.akrostis.append(z)
                            break

                    break
            print(reduce(lambda x,y : x+y,self.akrostis))
dosya = Dosya()
"""
Udemy:
    bas_harfler = ""

    with open("şiir.txt","r",encoding="utf-8") as file:
    for satır in file:
        bas_harfler += satır[0]
print(bas_harfler)
"""

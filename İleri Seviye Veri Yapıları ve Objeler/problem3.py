# -*- coding: utf-8 -*-
"""
Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

                    coskun.m.murat@gmail.com
                    example@xyz.com
                    mustafa.com
                    mustafa@gmail
                    kerim@yahoo.com

                           //
                           //
                           //


İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz.
"""
class Dosya():
    def __init__(self):
        with open("problem3.txt","r",encoding="utf-8") as file:
            dosya_icerik = file.readlines()
            #print(dosya_icerik)
            self.mailler = list()

            for i in dosya_icerik:
                #print(i.find("@"))
                i =i.strip("\n")
                if(i.find("@") != -1):
                    #print(i)
                    if(i.endswith(".com") and not(i.endswith("@.com"))):
                        #print(i)
                        self.mailler.append(i)

            for i in self.mailler:
                print(i)


dosya = Dosya()
"""
Udemy:
        for satır in file:
            satır = satır[:-1]
            if (satır.endswith(".com") and satır.find("@") != -1):
                print(satır)
"""

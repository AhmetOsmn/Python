# -*- coding: utf-8 -*-
"""
Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve soyisimleri isimlere göre sıralı bir şekilde yazdırmaya çalışın.

        isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
"""
isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
isimsoyisim = list()
for i,j in zip(isimler,soyisim):
    #print(i,j)
    a =i + " " + j
    isimsoyisim.append(a)

#print(isimsoyisim)
isimsoyisim.sort()
print(isimsoyisim)
"""
Udemy:
    isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

    soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

    liste = list(zip(isim,soyisim))

    liste.sort()

    for i,j in liste:
        print(i,j)
"""

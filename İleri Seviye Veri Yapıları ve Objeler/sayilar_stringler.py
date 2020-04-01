
#10luk tabandaki sayiyi 2lik tabanda gostermek istersek.
print(bin(4))
print(bin(44))

#10luk tabandaki sayiyi 16lik tabanda gostermek istersek.
print(hex(4))
print(hex(44))
print(hex(444))

#abs() fonksiyonu,mutlakdeger fonksiyonudur.
print(abs(-55))

#round() fonskiyonu,girilen float sayiyi yuvarlama yapar.
#(4.4 --> 4 , 4,5 -->5)
print(round(3.5))
print(round(44.556215))
print(round(3.2229,3)) #(x,3),3'e gore yuvarladik.

#max() fonksiyonu:girilen degerlerin en buyugunu dondurur.
#liste ve demetlerde de ayni sekilde calisir.
print(max(55,66,8,6,2,356,4,78,9,2,1,0,-55))
print(max([1,2,3,4,5,6,7,8,9]))

#min() fonksiyonu:girilen degerlerin en kucugunu dondurur.
#liste ve demetlerde de ayni sekilde calisir.
print(min(55,66,8,6,2,356,4,78,9,2,1,0,-55))
print(min([1,2,3,4,5,6,7,8,9]))

#sum() fonksiyonuna:iteresyon yapilabilen bir yapi;liste,demet vs.
#gonderdigimizde degerlerinin toplamini dondurur.
print(sum([1,2,3,4,5,6,7,8,9]))
print(sum(((1,2,3,4,5,6,7,8,9))))
print(sum([1,2,3,4,5,6,7,8,9,"Ahmet"])) #str ile int toplanamaz,hata verir.
print(sum([1,2,3,4,5,6,7,8,9,10.9]))

#pow() fonskiyonu:üs alma fonksiyonudur.pow(x,y)==x ** y
print(pow(2,4)) #2**4
print(pow(17,4))
print(pow(16,0.5))

"""
------------------------------STRINGLER------------------------------
"""

#upper() fonksiyonu:stringin butun karakterlerini buyuk harfe ceviriyor.
print("ahmet".upper())
print("osMaN".upper())

#lower() fonksiyonu:stringin butun harflerini kucuk harfe ceviriyor.
print("Ahmet".lower())
print("oSMAn".lower())

#replace(x,y) fonksiyonu:stringteki x karkterleri yerine y karakterini yaziyor.
print("Herkes ana baba baci gardes".replace("a","o"))
print("Python Programlama Dili".replace(" ","-"))
print("Kunduz".replace("duz","zun"))

#stratswith(x) fonksiyonu:eger stirng x karakteri ile basliyorsa True doner,baslamiyorsa False doner.
print("Ahmet".startswith("A"))
print("Osman Sezgin".startswith("A"))
print("Osman Sezgin".startswith("o"))#buyuk kucuge duyarli.
print("Osman Sezgin".startswith("O"))

#endswith(x) fonksiyonu:eger stirng x karakteri ile bitiyorsa True,bitmiyorsa Flase doner.
print("ahmet".endswith("t"))
print("osmaN".endswith("x"))
print("OSMan".endswith("n"))
print("ahmet".endswith("met"))

#split(x) fonksiyonu:x karakterine gore stirngi parcalara ayirir ve her parcayi listeye atar.
liste = "Python Programlama Dili".split(" ")
print(liste)
liste2 = "Ahmet-Osman-Sezgin".split("-")
print(liste2)

#strip(x) fonksiyonu:stringin basinda ve sonunda bulunan x degerlerini siliyor.
print("-------ahmet-------".strip("<"))
print("-------ahmet-------".lstrip("-"))
print("-------ahmet-------".rstrip("-"))

#join(x) fonksiyonu:listenin her helemaini x karakteri ile birlestirir.
liste = ["21","03","2000"]
print("/".join(liste))
liste2 = ["T","B","M","M"]
print(".".join(liste2))

#count(x) fonksiyonu:stringin icindeki x karakterinin sayisini dondurur.
print("Herkes ana baba baci gardas".count("a"))
print("Herkes ana baba baci gardas".count("a",10)) #saymaya 10. indeksten itibaren baslar.

#find(x) fonksiyonu:stringin icinde bastan itibaren aramaya baslar.Buldugu ilk indeksi dondurur,bulamazsa '-1'dondurur.
print("ahmet osman sezgin".find("a"))
print("ahmet osman sezgin".find("c"))
#rfind(x) fonksiyonu:stringin icinde sondan itibaren aramaya baslar.Buldugu ilk indeksi dondurur,bulamazsa '-1'dondurur.
print("ahmet osman sezgin".rfind("a"))
print("ahmet osman sezgin".rfind("c"))

# -*- coding: utf-8 -*-
"""
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

İpucu : Kodlama egzersizimizde buna çok benzer bir şey yapmıştık.
"""
def harf_frekans(a):
    harf_listesi = list()

    for i in a:
        #print(i)
        harf_listesi.append(i)

    #print(harf_listesi)
    harf_sozluk = dict()

    for i in harf_listesi:
        if(i in harf_sozluk):
            harf_sozluk[i] +=1
        else:
            harf_sozluk[i] = 1

    #print(harf_sozluk)

    for i in harf_sozluk:
        print("{} harfi {} kere geciyor..".format(i,harf_sozluk[i]))


stringg = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
harf_frekans(stringg)
"""
Udemy:
    s =  "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
    frekans = dict()

    for karakter in s:
        if (karakter in frekans):
            frekans[karakter] += 1
        else:
            frekans[karakter] = 1
    for i,j in frekans.items():
        print(i,":",j)
"""

def not_hesapla(satir):
    """
    #print(satir,end="")
    satir = satir[:-1]
    print(satir)
    """
    satir = satir[:-1]
    liste = satir.split(",")
    #print(liste)
    isim = liste[0]
    vize = liste[1]
    final = liste[2]
    son_not = float(vize) * (4/10) + float(final) * (6/10)

    if(son_not > 90):
        harf = "AA"
    elif(son_not >= 85):
        harf = "BA"
    elif(son_not >= 80):
        harf = "BB"
    elif(son_not >= 75):
        harf = "CB"
    elif(son_not >= 70):
        harf = "CC"
    elif(son_not >= 65):
        harf = "DC"
    elif(son_not >= 60):
        harf = "DD"
    elif(son_not >= 50):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "--------->" + " " + harf + " " + "\n"



with open("not_bilgileri.txt","r",encoding = "utf-8") as file:
    eklenecekler = []
    for i in file:
        eklenecekler.append (not_hesapla(i)) #her satiri fonksiyona gondermis olduk.

    print(eklenecekler) #liste seklinde yazdirdik

    with open("notlar.txt","w",encoding="utf-8") as file2:
        for i in eklenecekler:
            file2.write(i)

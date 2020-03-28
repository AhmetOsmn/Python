def takim_ayir(satir):
    satir = satir[:-1]
    liste = satir.split(" ")
    #print(liste)
    takim = liste[2]
    return takim

def isim(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    #print(liste)
    isim = liste[0]
    return isim + "\n" #Yazma isleminde alt alta yazmak icin + "|n" yaptik.

def ayir(satir):
    #print(satir)
    satir = satir[:-1] #\n den kurtulmak icin yapiyoruz.
    liste = satir.split(",")
    #print(liste)
    isim = liste[0]
    takim = liste[1]
    #print(takim)

    if(takim == "Galatasaray"):
        takimi = "Galatasaray"

    elif(takim == "Fenerbahçe"):
        takimi = "Fenerbahçe"
    else:
        takimi = "Beşiktaş"

    return isim + " " + "------->" + " " + takimi + " " +"\n"


with open("futbolcular.txt","r",encoding="utf-8") as file:
    bjk = []
    gs = []
    fb = []
    for i in file:
        #print(i)
        #print(ayir(i))
        #print(takim_ayir(ayir(i)))
        #print(isim(ayir(i)))
        if(takim_ayir(ayir(i)) == "Galatasaray"):
            gs.append(isim(i))
        elif(takim_ayir(ayir(i)) == "Fenerbahçe"):
            fb.append(isim(i))
        else:
            bjk.append(isim(i))

    #print(bjk)
    #print(gs)
    #print(fb)

    with open("Galatasaray.txt","w",encoding="utf-8") as file1:
        for i in gs:
            file1.write(i)

    with open("Fenerbahçe.txt","w",encoding="utf-8") as file2:
        for i in fb:
            file2.write(i)

    with open("Beşiktaş.txt","w",encoding="utf-8") as file3:
        for i in bjk:
            file3.write(i)
"""
Udemy Çözümü:

    gs = list()
    bjk = list()
    fb = list()

    for satır in file:
        satır = satır[:-1]
        satır_elemanları = satır.split(",")
        if (satır_elemanları[1] == "Fenerbahçe"):
            fb.append(satır + "\n")
        elif (satır_elemanları[1] == "Galatasaray"):
            gs.append(satır + "\n")

        else:
            bjk.append(satır + "\n")
    with open("gs.txt","w",encoding="utf-8") as file1:
        for i in gs:
            file1.write(i)



    with open("fb.txt","w",encoding="utf-8") as file2:
        for i in fb:
            file2.write(i)
    with open("bjk.txt","w",encoding="utf-8") as file3:
        for i in bjk:
            file3.write(i)
"""

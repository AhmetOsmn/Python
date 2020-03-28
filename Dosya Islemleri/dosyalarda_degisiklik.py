with open("bilgiler.txt","r+",encoding="utf-8") as file: #r+ kipi: hem okuma hem yazma yapacagÄ±m demek.
    print(file.read())

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    file.seek(10)
    file.write("Deneme") #10. karakterden sonra deneme yazdÄ±k:Ahmet OsmaDenemein
with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())


#Dosyanin son satirinin altine yeni satir eklemeye calisiyoruz.
with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())

with open("bilgiler.txt","a",encoding="utf-8") as file:
    file.write("Mert AltÄ±n\n") #a kipi ile ekleme yaptik,a kipi:imleci dosyanin sonuna goturuyordu.
with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())
with open("bilgiler.txt","a",encoding="utf-8") as file:
    file.write("Ulas Avil\n") #\n birakmamizin nedeni alt satira yeni bir sey eklenmek istenebilir.
with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    icerik = file.read()
    icerik = "Emre Doran\n" + icerik
    print(icerik)
# Ahmet Osman ' in uzerine bir satir eklemek:
with open("bilgiler.txt","r+",encoding="utf-8") as file:
    icerik = file.read()
    icerik = "Burak GÃ¼ney\n" + icerik
    file.seek(0)
    file.write(icerik)

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    print(liste)
    #insert() metodu ile herhangi bir indekse eleman ekleyebiliyoruz.

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"KÃ¼rÅat GÃ¼rler\n") #3.indekse kÃ¼rsat gÃ¼rler yaz.
    print(liste)

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(1,"Ahmet Sezgin\n")
    file.seek(0)
    for i in liste:
        file.write(i) #listedeki elemanlari tek tek dosyaya yaziyoruz.
with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(9,"Utku Hasa\n")
    file.seek(0)
    file.writelines(liste) #Direkt olarak dosyaya yazmak.

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())

#file = open("bilgiler.txt","w") #bilgiler.txt adında boş bir dosya oluşturduk.
#file.close() #dosyam kapanmis oldu.
#file_1 = open("C:/Users/Ahmet/Desktop/bilgiler.txt","w") #Dosya olusturmak istedigim yerin adresini yazarak oada olusturabilirim.
#file = open("bilgiler.txt","w",encoding = "utf-8") # w : yazma kipi,encoding = utf-8 : turkce karakterler yaziyorsak kullanacagımız kod.
#file.write("Ahmet Osman Sezgin")
#print(file.write("Ahmet Osman Sezgin")) uzunlugunu gösterir.
file = open("bilgiler.txt","w",encoding = "utf-8")
file.close()

file = open("bilgiler.txt","a",encoding="utf-8") #a kipi: dosyayi kapatmadan uzerine ekleme yapmak icin kullanilir.
file.write("Ahmet Osman Sezgin")
file.close()
file = open("bilgiler.txt","a",encoding="utf-8")
file.write("Reyhan Sezgin")
file.close()
file = open("bilgiler.txt","a",encoding="utf-8")
file.write("Sabri Sezgin")
file.close()

file = open("bilgiler.txt","w",encoding="utf-8")
file.write("Ahmet Osman Sezgin\n") #\n karakteri ile alt satira inmis oluruz.
file.close()

file = open("bilgiler.txt","a",encoding="utf-8")
file.write("Reyhan Sezgin\n")
file.close()

file = open("bilgiler.txt","a",encoding="utf-8")
file.write("Sabri Sezgin\n")
file.close()

file = open("bilgiler.txt","r") #file degikeni dosya uzerinde degisen imlec görevinde.
file.close()
#file = open("bilgiler2.txt","r") #bu isimde dosya olmadiginden hata alacagiz.
try:
    file = open("bilgiler2.txt","r")
except FileNotFoundError:
    print("Dosya Bulunamadi...")

file = open("bilgiler.txt","r",encoding="utf-8")
for i in file:
    print(i,end = "") #print fonksiyonu ile ekstra bir karakter(\n) koyma.
file.close()

file = open("bilgiler.txt","r",encoding="utf-8")
icerik = file.read() #read() dosyayi okuma fonksiyonu.
print("Dosyanin icerigi: ")
print(icerik)
print("Dosyanin icerigi 2: ")
icerik_iki = file.read()
print(icerik_iki) #file.read dedigimiz zaman ilk okumadan sonra file imleci en sona gidiyor.
                  #bu yuzden ikinci okumada bir sey gosukmuyor.
file.close()

file = open("bilgiler.txt","r",encoding="utf-8")

print(file.readline()) #
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline()) # dosyadaki satirlar bittikten sorna bosluk dondurur.

file.close()

file = open("bilgiler.txt","r",encoding="utf-8")
liste = file.readlines()
print(liste) #alt alta yazdigimizda python;\n otomatik olarak konuyor.
file.close()

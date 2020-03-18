print(35,5,88,47,75,sep = "/") #sep parametresi sayıların arasına belirtilen işaretin konulmasını sağlıyor.
print("06","04","2000",sep = "/")

print(*"Python") #* işareti her harfin arasına boşluk koyuyor.
print(*"Python",sep = "/") # * işareti ile sep i beraber kullanabiliriz.

print("T","B","M","M",sep = ".")
print(*"TBMM",sep = ".") #üstteki yapının daha pratik kullanımı

a = 3
b = 4
print("{} + {} 'nin toplamı {} 'dir".format(a,b,a+b)) #string formatlama denir.parantezler sırasıyla format() içindeki parametler ile eşleşir.
print("{}{}{}".format(3))

liste = [1,5,55]
print(len(liste))


liste_2 = list("Ahmet") # list fonksiyonu içine girdiğimiz stringi harf harf ayırıp lşste olusutrur
print(liste_2)

liste = [1,2,3,4,5,6,7,8,9,10]
print(liste[-1])

print(liste[4:])
print(liste[::2])
print(liste[:5])
print(liste[::-1]) #listeyi tersine çevirmiş olduk
print(liste*2)
liste[:2] = [15,16]
print(liste) # listenin 1. ve 2 indeksine direkt 15,16 değerlerini atadım
liste.append("python") #append() metodu listeye eleman eklememizi sağlıyor.
print(liste)
liste.append(1111)
print(liste)
liste.pop() #pop() metodu indeks girmezsek listenin son elemanını listeden atıyor,girersek girdiğimiz indeksteki elemanı atıyor
print(liste)
liste.pop()
print(liste)
liste.sort() #listeyi küçükten büyüğe sıralar.
print(liste)
liste.sort(reverse = True) #listeyi büyükten küçüğe sıralarız.
print(liste)

liste_2 = ["Ahmet","Osman","Sezgin","Ali","Beril"]
liste_2.sort() #stringlerden olusan listede alfabetik sıralama yapar.
print(liste_2)
liste = [[1,2],[3,4],[5,6]]
print(liste[0])#ilk listenin içine giriyoruz.[1,2] yazdı.
print(liste[0][1]) #[1,2] nin içine girip 2 yazdı.

demet = (1,2,3,4,5,6,7,8) #demetlerin özelliği sonradan değiştirme yapılamaz.
print(type(demet)) #demet in tipini yazdırır.(tuple)
print(demet)
print(demet[0])
print(demet[:-1])
print(demet[::2])
print(demet[::-1])
demet_2 = (1,1,1,1,1,1,2,2,4,5,5,5)
print(demet_2.count(1)) #count() metodu girilen eleman demette kaç kere tekrar etmiş onu geri döndürür.
demet_3 = ("Python","Php","C","Java")
print(demet_3.index("Java")) #index metodu girilen parametrenin kaçıncı indexte bulundugunu döndürür.

#sözlük = {} == sözlük = dict() aynı görevdelerdır.
sozluk = {"bir":1,"iki":2,"üç":3,"dört":4}
print(sozluk)
print(sozluk["bir"])
sozluk["beş"] = 5
print(sozluk) #sözlüklerde sıra yoktur.Gerek te yoktur.
a = {"bir":[1,2,3,4],"iki":[[1,2],[3,4],[5,6]],"üç":15}
print(a["bir"]) #[1,2,3,4]
print(a["bir"][1]) #2
a["bir"] = 5
print(a)
a["bir"] += 1
print(a)

a = {"Sayılar":{"bir":1,"iki":2,"üc":3},"meyveler":{"Kiraz":"yaz","portakal":"kış","erik":"yaz"}}
print(a["Sayılar"]) #{'bir': 1, 'iki': 2, 'üc': 3}
print(a["Sayılar"]["iki"]) # 2
print(a["meyveler"]["Kiraz"]) #yaz

sozluk = {"bir":1,"beş":5,"on":10,"yirmi":20}
print(sozluk)
print(sozluk.keys()) #keys() metodu sözlükteki anahtar kelimeleri döndürür.
print(sozluk.values()) #values() metodu sözlükteki değerleri döndürür.
print(sozluk.items()) #python demet oluşturarak keys ve value leri demete atıyor.

for k,v in sozluk.items():
    print(k,v)

a = input("sayi giriniz:")
print("girilen deger: ",a)

a = input("sayi giriniz:") #10
print(a * 3) #101010
print(type(a)) #a str olarak algılanıyor.

a = int(input("Sayi giriniz: ")) #10
print(a*3) #30

a = int(input("Birinci sayi: ")) #50
b = int(input("ikinci sayi: ")) #20
c = int(input("üçüncü sayi: ")) #30
a = int(input("Birinci sayi: ")) #35asdasdasd girerse hata alır.
print(a+b+c) #100

try:
    a = a = int(input("a: "))
    print(a)
except ValueError: #eger ValueError hatası dönecekse exceptten sonraki kısım uygulanır.
    print("Lütfen inputu sayi girin")

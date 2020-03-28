print(5 in [1,2,3,4]) #in oparotörü 5 in liste içinde olup olmadıgını kontrol eder.Varsa True,yoksa False döndürür.

liste = [1,2,3,4,5,6,7,8]
for eleman in liste: #pythona özel bir kullanım şekli.liste üzerinde gezinmek istiyorum demektir.
    print(eleman)

toplam = 0
liste = [1,2,3,4,5,6,7,8,9,10]

for eleman in liste:
    toplam = toplam + eleman
    print("Toplam: {} , En Son Eklenen Eleman: {} ".format(toplam,eleman))
print(toplam)

# % oparotörü kalan bulma opatotörüdür.
liste = [1,2,3,4,34,54,63,77,90]

for eleman in liste:
    if eleman % 2 == 0: #2'ye bölümünden kalanı 0 ise yazdır.(Çift sayıları)
        print(eleman)

s = "Ahmet"
for i in s:
    print(i)

s = "Ahmet"
for i in s:
    print(i*3)

demet = (1,2,3,4,5)
for a in demet:
    print(a)

liste = [(1,2),(3,4),(5,6),(7,8)]
#for eleman in liste:
#    print(eleman) #Her elemanımız demet oldu.

for (i,j) in liste: #demetlerin üzerinde gezinme yöntemi.
    print("i: {},j: {} ".format(i,j))

liste = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for (i,j,k) in liste:
    print("i: {} , j: {} , k: {} ".format(i,j,k))

liste = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for (i,j,k) in liste:
    print(i*j*k) # demetlerin içindeki degerleri çarpıyoruz.

sozluk = {"bir":1,"iki":2,"üc":3,"dort":4}

for eleman in sozluk: #sadece anahtarlar geldi,değerler gelmedi.
    print(eleman)

for eleman in sozluk.values():
    print(eleman)

sozluk = {"bir":1,"iki":2,"üc":3,"dort":4}
#print(sozluk.items())
for i,j in sozluk.items():
    print("Anahtar:",i,"Değer:",j)

liste = [1,2,3,4,5]

for i in liste:
    print(i)

    #yukarıdaki döngünün while şekli

index = 0
while(index < len(liste)):
    print(liste[index])
    index += 1 # eger index değerini arttırmasaydık sonsuz döngüye girerdik.

#print(*range(0,20)) #range() fonksiyonunun işlevi.
#print(*range(10)) # * işaretini kullanmazsak range() metodunun yaptıgı işlemi göremiyoruz.
#print(*range(20,0,-1)) #tersten gitmek için kullanılan yöntem.

for i in range(1,10):
    print("* " * i) #üçgen yazar.

while True: #sonsuz söngüde break ifadesinin kullanımı.
    isim = input("İsminizi girin(Çıkmak için q ya basın): ")
    if(isim == "q"):
        print("Programdan çıkılıyor...")
        break
    print("İsminiz: ",isim)

liste = [1,2,3,4,5]

for i in liste:
    if(i == 3 or i == 5):
        continue # 3 veya 5 oldugunda,döngüye yukarıdan tekrar basla.
    print(i)

i = 0
while(i < 10):
    if(i == 2):
        i +=1
        continue # i=2 de sürekli kalacagı için sonsuz döngüye girecek.Bu yüzden yukarıda i +=1  yapmak zorundayız.
    print(i)
    i +=1

liste_1 = [1,2,3,4,5]
liste_2 = [i for i in liste_1] # list comprehension yöntemi.
print(liste_2)
liste_3 = [i*2 for i in liste_1]
print(liste_3)

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste_1 = list()

for i in liste:
    for x in i:
        liste_1.append(x)
print(liste_1)
print("*****************************************************")
liste_2 = [x for i in liste for x in i] #yukarıdaki kodun list comprehension yöntmei ile yapılışı.
print(liste_2)


a = [1,2,3,4,5]
help(a.extend) #help() metodu bir metodun görevini unuttuğumuzda bize metodu açıklar.

def faktoriyel(sayi):
    faktoriyel = 1
    if(sayi == 0 or sayi == 1):
        print("Faktoriyel: ",faktoriyel)
    else:
        while(sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
        print("Faktoriyel: ",faktoriyel)

faktoriyel(5)

def toplama(a,b,c):
    return a + b + c
    print("Toplama Fonksiyonu..) # return kullanımından sonraki kısım işlenmez,atlanır.

def selamla(isim = "isimsiz"): #eger parametre verilmeden kullanılırsa varsayılan deger olarak "isimsiz"atanır.
    print("Selam: ",isim)
selamla()
selamla("Ahmet")

def bilgilerigoster(ad = "Bilgi yok",soyad = "Bilgi yok",numara = "Bilgi yok"):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)
bilgilerigoster("Ahmet")
bilgilerigoster("Ahmet","Sezgin")
bilgilerigoster("Ahmet","Sezgin","123456")
#bilgilerigoster(,,"123456") syntax hatası verdi.Bunun yerine alttaki kullanım var.
bilgilerigoster(numara = "123456") #Sadece numaramı göstermek istiyorsam bu şekilde kullanıyorum.Yukarıdaki kullanım yanlıştır.

#help(print) print fonksiyonunun kullanımı.
def toplama(*a): #farklı sayıda parametre kullanabiliriz.Demet olarak saklanıyor.
    print(a)
toplama(1,2,4,5)
toplama(2,5,8,9,3,7,8,6)

c = 10
def fonksiyon():
    c = 2 #eger global degişken ile local degişken aynı isimde ise fonksiyonun icinde  local olan kullanılır.
    print(c)
fonksiyon()
print(c)


d = 5
def fonksiyon():
    global d #artık globaldaki d kullanılmaya başlar.Ama bu kullanım tavsiye edilmez.
    d = 3
    print(d)
fonksiyon()
print(d)

liste_1 = [1,2,3,4,5] #klasik yöntem.
liste_2 = [i*2 for i in liste_1] #list comprehension yöntemi.
print(liste_1)
print(liste_2)

def ikiylecarp(x):
    return x * 2
print(ikiylecarp(3))

ikiylecarp = lambda x : x * 2 #lambda kullanımı ile yukarıdaki fonksiyonun kullanımı
print(ikiylecarp(3))

toplama = lambda a,b,c : a+b+c #lambda yöntemi
print(toplama(5,6,8))

terscevir = lambda s : s[::-1]
print(terscevir("Ahmet"))

ciftmi_tekmi = lambda sayi : sayi % 2 == 0
print(ciftmi_tekmi(13))

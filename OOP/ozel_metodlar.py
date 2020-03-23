class Kitap():
    #pass
    def __init__(self,isim,yazar,sayfa,tür):
        print("__init__ fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa = sayfa
        self.tür = tür

    def __str__(self): #__Str_ metodunu kenim tekrar yazmis oldum.
        return "İsim: {}\nYazar: {}\nSayfa sayisi: {}\nTürü: {}".format(self.isim,self.yazar,self.sayfa,self.tür)

    def __len__(self):
        return self.sayfa

    def __del__(self):#pythondaki __del__ metoduna ekstra bir seyler ekliyorum.
                      #Diger metodlardan farklıdır.(__len__,__str__,__init__)

        print("Kitap objesi siliniyor...")



kitap = Kitap("İstanbul Hatirasi","Ahmet Ümit",561,"Polisiye")




kitap = Kitap() #__init__ metodu otomatik olarak cagirildi.

print(kitap) #__str__ metodu python tarafından otomatik oalrak tanımlanmış.
             #ekrana <__main__.Kitap object at 0x0000023701DB1888> yazdi.

len(kitap) #__len__ metodunu cagirmak istiyor ama tanimli olmadigi icin cagiramiyor.
           #ekrana object of type 'Kitap' has no len() hatasını verir.

del kitap #__del__ metodunu otomatik cagirarak kitap obejisini siliyor.

print(kitap)

print(kitap) #<__main__.Kitap object at 0x0000023701DB1888> yazmamasi icin ben kendim __str__ metodunu olusturdum.
print(len(kitap)) #len(kitap) şeklinde kullandigimda hata vermemesi icin kitap classında __len__ metodunu kendim tanimladim.

#http://www.diveintopython3.net/special-method-names.html metodların kullanımlarını anlatan site.

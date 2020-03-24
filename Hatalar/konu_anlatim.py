#a = int("asdasdasdasd") #ValueError

try:
    a = int("asdasd132ads")
    print("Program burada")
except:
    print("Bir hata olustu")
print("Program kapatiliyor..")


try:
    a = int("444")
    print("Program burada")

except:
    print("Bir hata olustu")
print("Bloklar sona erdi..")


try:
    a = int("asdasd132ads") #ValueError
    print("Program burada")

except ValueError:
    print("Bir hata olustu")
print("Program kapatiliyor..")

#print(2/0) #ZeroDivisionError

try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a/b)
except ValueError:
    print("Lütfen inputu dogru girin")
except ZeroDivisionError:
    print("Bir sayi sifira bolunemez..")
print("Bloklar sona erdi")

try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a/b)
except (ValueError,ZeroDivisionError): #İki hatayı tek except ile kontrol edebiliriz.
                                       #Fakat genellestirmek yerine ozellestirmek daha kullanislidir.
    print("Lütfen inputu dogru girin")
print("Bloklar sona erdi")

try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a/b)
except ValueError:
    print("Lütfen inputu dogru girin")
except ZeroDivisionError:
    print("Bir sayi sifira bolunemez..")
finally: #Her ne olursa olsun calısacak kodlari yazdigimiz kisim.
         #Mesela,bir dosyayi kapatmamiz gerektigi yerlerde.
    print("Burasi calisti")
print("Bloklar sona erdi")



def ters_cevir(s):
    if(type(s) != str):
        raise ValueError("Lütfen string bir deger gonderin.")
    else:
        return s[::-1]

print(ters_cevir("Ahmet"))
print(ters_cevir(2123))

def ters_cevir(s):
    if(type(s) != str):
        raise ValueError("Lütfen string bir deger gonderin.") #raise: hata fırlatma,("istedigimiz aciklama")
    else:
        return s[::-1] #strigni ters cevirir

try:
    print(ters_cevir(12))
except ValueError:
    print("Fonksiyon hata verdi.")

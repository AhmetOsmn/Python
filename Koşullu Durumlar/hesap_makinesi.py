print("""*******************************
Hesap Makinesi Programi

islemler

1.Toplama islemi

2.Cikartma islemi

3.Carpma islemi

4.Bolme islemi


*******************************""")
a = int(input("birinci Sayi: "))
b = int(input("ikinci Sayi: "))

islem = input("islemi seciniz: ") #Burada inputu int'e cevirmedigimiz  icin if kosullarinda str olarak kontrol etmek zorundayiz.

if islem == "1": #str olarak kontrol etmek zorundayiz.
    print("{} ile {} in toplami {} dir.".format(a,b,a+b))
elif islem == "2": #str olarak kontrol etmek zorundayiz.
    print("{} ile {} in farki {} dir.".format(a,b,a-b))
elif islem == "3": #str olarak kontrol etmek zorundayiz.
    print("{} ile {} in carpimi {} dir.".format(a,b,a*b))
elif islem == "4": #str olarak kontrol etmek zorundayiz.
    print("{} ile {} in bolumu {} dir.".format(a,b,a/b))
else:
    print("Gecersiz islem...")

boy = float(input("Boyunuzu m cinsinden giriniz: " ))
kilo = float(input("Kilonuzu kg cinsinden giriniz: "))

vki = kilo / (boy*boy)
print(vki)

if(vki < 18.5):
    print("Zayıf")
elif(vki > 18.5 and vki < 25):
    print("Normal")
elif(vki > 25 and vki < 30):
    print("Fazla Kilolu")
else:
    print("Obez")

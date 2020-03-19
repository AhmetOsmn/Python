cevap = input("Üçgen mi,Dörtgen mi: ")

if(cevap == "Dörtgen"):
    a = float(input("Birinci Kenar: "))
    b = float(input("İkinci Kenar: "))
    c = float(input("Üçüncü Kenar: "))
    d = float(input("Dördüncü Kenar: "))

    if(a == b and a == c and a ==d):
        print("Kare")
    elif(a == b and c == d or a == c and b == d):
        print("Dikdörtgen")
    else:
        print("Sıradan bir dörtgen")

elif(cevap == "Üçgen"):
    a = float(input("Birinci Kenar: "))
    b = float(input("İkinci Kenar: "))
    c = float(input("Üçüncü Kenar: "))
    if(abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c  < a+b):
        if(a == b and a == c and b == c):
            print("Eşkenar üçgen")
        elif(a == b and a != c or a == c and a != b or b == c and b != a):
            print("İkizkenar Üçgen")

    else:
        print("Üçgen Belirtmiyor...")


else:
    print("Geçersiz şekil...")

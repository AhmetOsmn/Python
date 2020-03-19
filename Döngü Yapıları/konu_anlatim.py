print("""***************************

Atm makinesine hosgelidniz.

İslemler;

1.Bakiye sorgulama

2.Para yatirma

3.Para cekme

Programdan cikmak icin q ya basiniz...
***************************""")

bakiye = 1000

while True:
    islem = input("İslem seciniz: ")
    if (islem == "q"):
        print("iyi günler")
        break
    elif(islem == "1"):
        print("Bakiyeniz {} tldir.".format(bakiye))
    elif(islem == "2"):
        miktar = int(input("Miktar giriniz: "))
        bakiye += miktar
    elif(islem == "3"):
        miktar = int(input("Miktar giriniz: "))
        if(bakiye - miktar < 0 ):
            print("Böyle bir miktar cekemezsiniz..")
            continue
        bakiye -= miktar
    else:
        print("Gecersiz islem")

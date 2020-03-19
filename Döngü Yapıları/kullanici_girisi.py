print("""**********************************

Kullanici Girisi

**********************************""")

sys_kullanici_adi = "Ahmet"
sys_parola = "123456"
giris_hakki = 3

while True:
    kullanici_adi = input("Kullanici adi: ")
    parola = input("Parola: ")

    if(kullanici_adi != sys_kullanici_adi and parola == sys_parola):
        print("kullanici adi hatali...")
        giris_hakki -=1
        print("Kalan giris hakkiniz: {} ".format(giris_hakki))
    elif(kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola hatali...")
        giris_hakki -=1
        print("Kalan giris hakkiniz: {}".format(giris_hakki))
    elif(kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanici adi ve Parola hatali...")
        giris_hakki -=1
        print("Kalan giris hakkiniz: {}".format(giris_hakki))
    else:
        print("sisteme giris yapıldı...")
        break
    if(giris_hakki == 0):
        print("Giris hakkiniz bitti...")
        break

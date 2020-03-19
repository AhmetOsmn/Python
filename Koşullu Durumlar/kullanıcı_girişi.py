print("""***********************
Kullanıcı Girişi
***********************
""")

sys_kullanici_adi = "ahmet"
sys_parola = "12345"

kullanici_adi = input("Kullanıcı Adı: ")
parola = input("Parola: ")

if(kullanici_adi == sys_kullanici_adi and parola != sys_parola):
    print("Hatalı şifre girdiniz...")
elif(kullanici_adi != sys_kullanici_adi and parola == sys_parola):
    print("Hatalı kullanıcı adı girdiniz...")
elif(kullanici_adi != sys_kullanici_adi and parola != sys_parola):
    print("Kullanıcı adı ve parola hatalı...")
else:
    print("Giriş yapıldı...")

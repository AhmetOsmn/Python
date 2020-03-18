print("Oyuncu kaydetme")
ad = input("Oyuncunun adı: ")
soyad = input("Oyuncunun soyadı: ")
takım = input("Oyuncunun takımı: ")

bilgiler = [ad,soyad,takım]

print("Bilgiler kaydediliyor...")
print("\n")
print("Oyuncunun Adı: {} \nOyuncunun Soyadı: {} \nOyuncunun Takımı:{}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))
print("Bilgiler kaydedildi...")

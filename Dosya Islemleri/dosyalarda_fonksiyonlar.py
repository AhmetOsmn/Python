#Dosyayi otomarik kapatma:

with open("bilgiler.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i)

with open("bilgiler.txt","r",encoding="utf-8") as file:
    print(file.tell()) #tell():file imlecinin nerede oldugunu soyler.

with open("bilgiler.txt","r",encoding="utf-8") as file:
    print(file.tell()) #tell():file imlecinin nerede oldugunu soyler.
    file.seek(20) #file imleci 20.byte'a gitmis oldu.
    print(file.tell())

with open("bilgiler2.txt","r",encoding="utf-8") as file:
    file.seek(5)
    icerik = file.read(10) #10byte'lik okuma yap.(10 karakter)
    print(icerik)


with open("bilgiler2.txt","r",encoding="utf-8") as file:
    file.seek(5)
    icerik = file.read(10) #10byte'lik okuma yap.(10 karakter)
    print(file.tell())
    print(icerik)

with open("bilgiler2.txt","r",encoding="utf-8") as file:
    file.seek(5)
    icerik = file.read(10) #10byte'lik okuma yap.(10 karakter)
    file.seek(0) #file imlecini dosyanin basina geri aldik.
    icerik2 = file.read(6)

    print(icerik)
    print(icerik2)


print(bool(14)) # bool() metodunun içerisine girdiğimiz değeri 0 ile kıyaslar eğer farklıysa true döndürür.
a = None #a değişkenine sonradan değer atama yapmak istiyorsak kullanılır.
print(a)

print(1 > 2 and "Ahmet" < "Zula" and 4.32 < 5.66)
print(1 < 2 and "Ahmet" > "Zula" and 4.32 < 5.66) #Python da pratik bir yöntem var,and bağalcını kontrol ederken false ifade gördükten sonra geri kalanı kontrol etmez false çıkarır.
print(1 < 2 or "Ahmet" < "Zula" or 4.32 > 5.66) #Python da pratik bir yöntem var,or bağalcını kontrol ederken True ifade gördükten sonra geri kalanı kontrol etmez True çıkarır.

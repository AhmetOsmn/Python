def tam_bolenler(sayi):
    tam_bolenler = []
    for i in range(2,int(sayi/2)+1):
        if(sayi % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

while True:
    sayi = input("Sayi:")
    if(sayi == "q"):
        pirnt("Kapatılıyor")
        break
    else:
        sayi = int(sayi)
        print("Tam bolenleri  :",tam_bolenler(sayi))

    

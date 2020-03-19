print("""*************************

Faktoriyel Bulma Programi

*************************""")

while True:
    sayi = input("Sayi: ")
    if(sayi == "q"):
        print("Program sonlaniyor...")
        break
    else:
        sayi = int(sayi)
        fakt = 1

        for i in range(1,sayi+1):
            print("Faktoriyel",fakt," carpilacak sayi",i)
            fakt *= i
        print("Faktoriyel: ",fakt)

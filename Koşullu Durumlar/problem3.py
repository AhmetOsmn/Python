
vize1 = int(input("Vize 1: "))
vize2 = int(input("Vize 2: "))
final = int(input("Final: "))

toplam_not = vize1*(3/10)+vize2*(3/10)+final*(4/10)


if(toplam_not >= 90):
    print("AA")
elif(toplam_not >= 85):
    print("BA")
elif(toplam_not >= 80):
    print("BB")
elif(toplam_not >= 75):
    print("CB")
elif(toplam_not >= 70):
    print("CC")
elif(toplam_not >= 65):
    print("DC")
elif(toplam_not >= 60):
    print("DD")
elif(toplam_not >= 55):
    print("FD")
elif(toplam_not < 55):
    print("FF")

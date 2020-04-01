#append() metodu:listenin en sonuna eleman ekler.
liste = [1,2,3,4,5]
liste.append(6)
print(liste)
liste.append("Ahmet")
print(liste)

#extend() metodu:listeden listeye ekleme yapar.
liste1 = [1,2,3,4,5,6,7]
liste1.extend([10,11,12])
print(liste1)

#insert() metodu:listenin herhangi bir yerine ekleme yapar.
liste = [1,2,3,4,5,6,7,8]
liste.insert(2,"Ahmet") #2. indekse
print(liste)

#pop() metodo:listeden eleman cikartmamizi saglar.
liste = [1,2,3,4,5,6,7]
liste.pop() #bos birakirsak son elemani siler.
print(liste)
liste.pop(2) #2.indeksteki elemani siler
print(liste)

#remove() metodu:girilen elemani listeden cikartir.
liste = ["AHMET","OSMAN","SEZGIN"]
liste.remove("AHMET")
print(liste)
#liste.remove("osman") #listede olmadigi icin hata doner.

#index() metodu:girilen elemanin indeksini verir.
liste = ["ahmet","osman","sezgin"]
print(liste.index("osman"))

liste2 = [1,2,3,4,3,3,5,6,7,8,9]
print(liste2.index(3,3)) #3.indeksten basla

#count() metodu:girilen degerin listede kac defa gectigini sayiyor.
liste = [1,2,34,5,6,7,8,3,1,2,1,2,1,4,5,6,7,3,2,2]
print(liste.count(2))

#sort() metodu:listeyi kucukten buyuge siralar.
liste = [12,-2,3,1,34,100]
liste.sort()
print(liste)

liste2 = ["Python","Java","Php","C"]
liste2.sort()
print(liste2)

liste.sort(reverse = True) #listeyi buyukten kucuge siralar.
print(liste)
liste2.sort(reverse = True)
print(liste2) 

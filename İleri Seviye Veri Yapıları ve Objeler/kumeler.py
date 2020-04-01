#kumeler bir elemandan sadece 1 tane turar.
x = {1,2,3} #kume -> set
print(type(x))

liste = [1,2,3,3,1,1,2,2,2]
x = set(liste)
print(x) #{1,2,3}

x = set("Python Programalama Dili")
print(x)

x = {"Elma","Armut","Kiraz","Muz"}
for i in x:
    print(i) #kumeler sirasiz olarak tutulur.

#kumenin elemanlarini for dongusu ile veya listeye cevirip erisebiliriz.
x = {"Python","Php","Java","Javascript"}
liste = set(x)
print(liste)

#add() metodu:kumeye ekleme yapmamizi saglar.Ayni eleman var ise eklemez.
x = {1,2,3}
x.add(6)
x.add(6)
print(x)

#kume1.difference(kume2) metodu:kume1 in kume2 denf arkini doner.
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
print(kume1.difference(kume2)) #kume1 de olup kume2 de olmayanlar.
print(kume2.difference(kume1))

#kume1.difference_update(kume2) metodu:kume1'e,kume1'in kume2'den farkini atar.
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
kume1.difference_update(kume2)
print(kume1)

#discard(x) metodu:kumeden x degerini cikart.Eger kumede x yok ise hicbir sey yapmaz.
x = {1,2,3,4,5,6,7}
x.discard(2)
print(x)
x.discard(5)
print(x)
x.discard(222)
print(x)

#kume1.intersection(kume2) metodu:iki kumenin kesisimin verir.
x = {1,2,3,4,5,6,7,8,9,10,11}
y = {6,7,8,9,10,11,12,13,14,15}
print(x.intersection(y))

#kume1.intersection_update(kume2) metodu:x kumesine,iki kumenin kesisimini atar.
x = {1,2,3,4,5,6,7,8,9,10,11}
y = {6,7,8,9,10,11,12,13,14,15}
x.intersection_update(y)
print(x)

#kume1.isdisjoint(kume2) metodu:kumeler ayrik ise True,ayrik degil ise yani kesisimleri bos kume degil ise Flase doner.
x = {1,2,3,4,5,6,7,8,9,10,11}
y = {6,7,8,9,10,11,12,13,14,15}
print(x.isdisjoint(y))
x = {1,2,3,4,5,6,7,8,9,10,11}
y = {12,13,14,15}
print(x.isdisjoint(y))

#kume1.issubset(kume2) metodu:kume1,kume2 nin alt kumesi ise True,degil ise False dondurur.
x = {1,2,3}
y = {1,2,3,4}
z = {5,6,7}
print(x.issubset(z))
print(x.issubset(y))

#kume1.union(kume2) metodu:iki kumenin birlesimini almamizi saglar.
x = {1,2,3,10,34,100,-2}
y = {1,2,23,34,-1}
print(x.union(y)) #ortak elemanlar sadece 1 defa kullanilacak.

#kume1.update(kume2) metodu:iki kumenin birlesimini bulacak ve birlesimi kume1'e atacak.
x = {1,2,3,10,34,100,-2}
y = {1,2,23,34,-1}
x.update(y)
print(x)

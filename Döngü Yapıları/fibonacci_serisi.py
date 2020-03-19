a = 1
b = 1

fibo = [a,b]
hedef = int(input("Kacinci sayiya kadar bulunsun: "))

for i in range (hedef):
    a,b = b,a+b
    fibo.append(b)

print(fibo)

#1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
liste = [1,2,3,4,5,6,7,8,9,10]

for i in liste:
    print("*******************************")
    for j in liste:
        print("{}x{}={} ".format(i,j,i*j))
    print("*******************************")

"""
Udemy cözümü:

    for i in range(1,11):
    print("*************************************************")
    for j in range(1,11):

        print("{} x {} = {}".format(i,j,i*j))

"""

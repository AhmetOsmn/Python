liste = ["345","sadas","324a","14","kemal"]

for i in liste:
    try:
        i = int(i) #ValueError
        print(i)
    except:
        pass
 

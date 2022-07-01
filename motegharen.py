def determiner(n,arayeh):    
    m =int(n/2)
    flag = 0
    for i in range(m):
        if arayeh[i] != arayeh[n-1]:
            print("motegharen nist")
            flag = 1
            break
        else:
            n-= 1
    if flag == 0:
        print('motegharen')

n = int(input('n:'))
arayeh = []
for i in range(n):
    x = int(input('insert the nember: '))
    arayeh.append(x)
determiner(n,arayeh)
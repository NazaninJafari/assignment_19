import random

i = 7
girls = ['Maryam','Roya','Negar','Neda','Mahsa','Adeleh','Aynaz']
boys = ['Ali','Amir','Behrouz','Danyal','Babak','Kaveh','Hadi']
result =[]

while i>0 :   
    x = random.choice(girls)
    y = random.choice(boys)
    result.append([x,y])
    
    girls.remove(x)
    boys.remove(y) 
    i -= 1

for i in range(7):
    print(result[i])
def divide(x):
    a=x//1000
    b=(x//100) -(10*a)
    c=(x//10) -(100*a)-(10*b)
    d=(x//1) -(1000*a)-(100*b)-(10*c)
    
    return a,b,c,d
   # print(a,b,c,d)


for i in range (1000,10000):
    a,b,c,d=divide(i)
    if a==d and b==c :
        print(a,b,c,d)
        
    

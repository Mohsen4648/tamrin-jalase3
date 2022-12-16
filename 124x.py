def divide(x):
    a=x//100
    b=(x//10)-(10*a)
    c=(x//1)-(100*a)-(10*b)
    
      
    return a,b,c

def fish(a,b,c):
    if c>a+b :
        print (a,b,c)
    
for i in range(100,1000):
    a,b,c=divide(i)
    fish(a,b,c)


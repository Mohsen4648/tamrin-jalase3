def give():
    a=int(input("give me a number :"))
    return a

def great(a,b): 
    """divide smallest from biggest """
    if a>b :
        return a,b
    else :
        a,b = b,a
        return a,b
    
def BMM(a,b):
    """BMM means biggest common divided of two number"""
    c,d=great(a,b)    
    e=c%d
    if e != 0 :
                c,d = d,e
                e=c%d
               # print(e)
                return e
                
    elif e == 0:
        e = 1
        return e
            
    elif e == 1:
        return 1
            
def LCM(a,b):
    """LCM means ****************  """
    if BMM(a,b)>0:
       k=int((a/BMM(a,b))*(b/BMM(a,b))*(BMM(a,b)))
    return k

a=give()
b=give()
c=BMM(a,b)
k=LCM(a,b)

print(a,b,c,k)
print("LCM between "+str(a)+" and "+str(b)+" is : " +str(k))


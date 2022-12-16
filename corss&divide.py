def give():
    a=int(input("give me a number :"))
    return a

def cross_divide(a,b):
    
    if b!=0:
        c=float((a*b)-(a/b))
        return c
    else :
        print ("choose another number")
 
a=give()
b=give()

            
#print ("a*b = " + str(a*b))
#print ("a/b = " + str(a/b))
#print ("now diffrent between a*b & a/b :")
#print (str((a/b)((b^2)-1)))
     # """(a*b) - (a/b) === (a/b)*( b^2  - 1)"""


c=cross_divide(a,b)
print (str(c))



      
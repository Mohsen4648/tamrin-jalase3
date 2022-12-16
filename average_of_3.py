def give():
    a=int(input("give me a number :"))
    return a

def average(a,b,c):
    av=float((a+b+c)/3)
    return av
 
a=give()
b=give()
c=give()
av=average(a,b,c)

print ("average of this 3 numbers is : " + str(av))
def give(): # for give a number to see all divisor
    n=int(input("give a number : "))
    return n

def maghsum(n): # maghsum means divisor
    """ you can see All divisor of  a Number plus Number of them  and Sum of them """
    tedad=0  # tedad means how many
    jam=0 #jam means Sum
    for i in range(1,n+1):
        if n%i == 0 :
            tedad +=1
            # print(i,end=" ")
            jam +=i
    
    return[tedad,jam]

def before(n):
    t=0
    j=0
    a=[]
    
    for i in range(1,n+1):
        a[:]=maghsum(i)
        t+=a[0]
        j+=a[1]
    print(t,j)

n=give()
before(n) # tamame maghsum haye adad ghabl az n 

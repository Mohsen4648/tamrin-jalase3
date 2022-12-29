def give():
    n=int(input("give a number : "))
    return n

def maghsum(n):
    tedad=0
    jam=0
    for i in range(1,n+1):
        if n%i == 0 :
            tedad +=1
            print(i,end=" ")
            jam +=i
    print(end="\n")        
    print(tedad,jam)
n=give()
maghsum(n)


def give():
    a=int(input("give me a 3digits Number :"))
    if a<100 :
        print ("wrong Number")
        pass
    return a


def divide(x):
    if x<100 :
        print ("wrong Number")
        pass
    a=x//100
    b=(x//10)-(10*a)
    c=(x//1)-(100*a)-(10*b)
    
    print(a,b,c)   
    return a,b,c


a=give()
divide(a)
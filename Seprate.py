def give():
    a=int(input("give me a number :"))
    return a

def divide(x):
    y=len(str(x))
    l=[]
    for i in range (y):
        c=x//(10**(y-i-1))
        l.append(c)
        x=x-(c*(10**(y-i-1)))
    return l

print(divide(give()))
# x=give()        
# divide(x,y)
# print(divide(x))
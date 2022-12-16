def give():
    a=int(input("give me a number :"))
    return a


def great(a,b):
    if a>b :
        return a,b
    else :
        a,b = b,a
        return a,b

a=give()
b=give()
c=give()

d=great(great(a,b),great(a,c))

print (str(great(a,b)),str(great(a,c)))
print(d)

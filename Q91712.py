x=list(map(int,input().split()))
x1=x[0]
x2=x[1]

if x1==x2:
    print("Saal Noo Mobarak!")
elif x1>x2 :
    l=x1-x2
    print(l*"L")
else:
    r=x2-x1
    print(r*"R")
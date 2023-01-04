from math import trunc
a=list(map(int,input().split()))
n=a[0]
k=a[1]

z=n/(2*k)

if z >= 0:
    print(trunc(z))
else :
    print(round(z))

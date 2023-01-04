a=list(map(int,input().split()))
y=int(input(""))
P=a[0]
L=a[1]

for i in range (y):
    r=(P*2)-L
    P=r
    
print(P)

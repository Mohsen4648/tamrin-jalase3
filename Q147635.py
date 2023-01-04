n=int(input(""))
t=list(map(int,input().split()))

for i in range (n):
    if t[i] > 15:
        print("cooler")
    else :
        print("heater")

a=int(input("give me a Number :"))
for i in range (a,0,-1):
    print(i*" ",(a-i)*"*",(a-i)*"*",i*" ",end='\n')
for i in range (a):
    print(i*" ",(a-i)*"*",(a-i)*"*",i*" ",end='\n')        
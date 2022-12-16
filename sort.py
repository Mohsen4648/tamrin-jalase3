a=int(input("give me a number :"))
b=int(input("give me a number :"))
c=int(input("give me a number :"))
if a>b :
    if b>c :
        print( a , b, c )
    elif c>b :
        print( a , c, b )
elif b>a :
    if a>c :
        print ( b , a, c)
    elif c>a :
        print ( b , c, a )        
elif c>a :
    if a>b :
        print( c , a, b )
    else :
        print( c , b, a )
         
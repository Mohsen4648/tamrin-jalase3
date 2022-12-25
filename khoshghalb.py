def give():
    a=int(input("give a Number :"))
    return a

a=give()
if 0 < a < 100 :
    for i in range (a):
     print ("man khoshghlab hastam ")
else :
    print("wrong Number")
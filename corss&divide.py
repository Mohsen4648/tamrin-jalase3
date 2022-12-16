def give():
    a=int(input("give me a number :"))
    return a

a=give()
b=give()

print ("a*b = " + str(a*b))
print ("a/b = " + str(a/b))
print ("now diffrent between a*b & a/b :")
print (str((a/b)((b^2)-1)))
      #"""(a*b) - (a/b) === (a/b)*( b^2  - 1)"""
      
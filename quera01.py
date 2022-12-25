def give():
    a=int(input(""))
    return a
 
def givelist():
   a=[]
   for i in range (4):
      a.append(give())
   return a

def sum(a):
    sum=0
    for i in range (4):
        sum += a[i]
    return sum

def product(a):
    p=1
    for i in range (4):
        p*=a[i]
    return p

def max(a):
    max=0    
    for i in range (4):
            if a[i] > max :
                max = a[i]
    return max         

def min(a):
    min=1001    
    for i in range (4):
            if a[i] < min :
                min = a[i]
    return min         


x=givelist()

print(f"Sum : {sum(x) :.6f}")
print(f"Average : {(sum(x)/4) :.6f}")
print(f"Product : {product(x) :.6f}")
print(f"Max : {max(x) :.6f}")
print(f"min : {min(x) :.6f}")

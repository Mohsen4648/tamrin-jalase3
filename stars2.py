a=int(input("give me a Number :"))

for i in range(a):
    print ((a-i)*"*",((2*i)+1)*"#",(a-i)*"*")
    """first idea about half up of this shape"""
for i in range (a,-1,-1):
    print ((a-i)*"*",((2*i)+1)*"#",(a-i)*"*") 
    # this loop for half down
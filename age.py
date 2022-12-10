ynow=int(input("this year : "))
mnow=int(input("this month : "))
dnow=int(input('today :'))
yold=int(input("your bithday year : "))
mold=int(input("your bithday  month : "))
dold=int(input('your bithday day :'))
yage=int(ynow-yold)
mage=int(mnow-mold)
dage=int(dnow-dold)
if dage < 0 :
    mage = mage - 1
    dage = 30 + dage
    
print(yage,mage,dage)
#bayad tarikh check shavad baraye rooze manfi
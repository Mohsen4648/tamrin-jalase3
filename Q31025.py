# This program is answer of this question https://quera.org/problemset/31025/

from math import floor
a = list(map(int,input().split()))
print(floor(a[0]/(2**a[1])))
# n=a[0]
# k=a[1]

# z=n/(2*k)

# if z >= 0:
#     print(trunc(z))
# else :
#     print(round(z))


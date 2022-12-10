from datetime import date 
from datetime import time

nowdate = date.today()
nowtime = time(hour=int(hour()),minute=int(min()),second=int(second()))

print (nowdate)
print (nowtime)

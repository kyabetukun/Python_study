### 日付、時間 ###
from datetime import date,time,datetime
import jpholiday

#date
d = date(2021,3,14) #dateはyear,month,dayを持っている
print(d)

#time
t = time(12,15,10)#timeはhour,minute,second,microsecondを持っている
print(t)

#datetime
n = datetime(2022,12,4,14,1)
d2 = n.date()
print(d2)

#祝日
result = jpholiday.year_holidays(2023)
print(len(result))
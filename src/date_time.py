### 日付、時間 ###
from datetime import date,time,datetime
from dateutil.relativedelta import relativedelta
import calendar
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

#相対的に何日後かを取得
today = datetime.today()
d1 = today + relativedelta(days = 1)
d2 = today - relativedelta(days = 1)
print(d1)
print(d2)
today_str = d2.strftime('%Y/%m/%d')
print(today_str)
#2月の開始日と最終日を取得
c = calendar.monthrange(2020,2)
print(c[1])
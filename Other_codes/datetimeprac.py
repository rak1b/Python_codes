from datetime import datetime, date, time,timedelta

# import datetime

# n = datetime.datetime(2020,12,21)
# print(n)
# 
# now = datetime.datetime.today()
# print(now)

now = datetime.now()
print(now)

today = date.today()
print(today)

# print(datetime.utcnow())
timedel =timedelta(days=3)
timedelMonth = timedelta(days=30)

three_days_ago = today - timedel
thirty_days_ago = today - timedelMonth

print(three_days_ago)
print(thirty_days_ago)

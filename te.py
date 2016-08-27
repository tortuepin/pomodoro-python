import datetime

d = datetime.datetime.today()
a = d.replace(year = 2011)
c = datetime.datetime.today().replace(year = 2011, minute = 0, second = 0, microsecond = 0)
k = datetime.datetime.today().hour

print(c)
c = c.replace(day = datetime.datetime.today().day + 1)
print(c)

import datetime
x = datetime.datetime.now() - datetime.timedelta(days=1)
y = datetime.datetime.now()
z = datetime.datetime.now() + datetime.timedelta(days=1)
print(x.strftime("%D"))
print(y.strftime("%D"))
print(z.strftime("%D"))

import datetime

current=datetime.datetime.now()

print(datetime.date.today().month)

print(current.strftime("%d:%m:%Y"))

x=datetime.date.today()
print(x)
print(datetime.datetime.now().strftime("%b"))
print(datetime.datetime.now().strftime("%B"))

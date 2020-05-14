import datetime

now = datetime.datetime.now()
print("Current date and time is :")
print(now.strftime("%y-%m-%d"))
print(now.strftime("%H:%M:%S"))

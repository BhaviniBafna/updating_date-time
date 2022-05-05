import datetime
hr=int(input("enter hours: "))
min=int(input("enter minutes: "))
launchtime = datetime.datetime(2022, 5, 3, hr, min, 0)
print("Original time:")
print(launchtime)  
time_change = datetime.timedelta(hours=2,minutes=20)
destroy_time = launchtime + time_change
print("spaceship destroyed at:")
print(destroy_time)
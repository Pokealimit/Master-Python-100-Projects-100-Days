import datetime as dt

now = dt.datetime.now() # Return datetime type
year = now.year         # Return 'int' type
month=now.month
day_of_week = now.weekday()

print(type(now))
print(type(year))
print(type(day_of_week))

if year == 2021:
    print("Please wear a face mask")

# Create datetime object
date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)
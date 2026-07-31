import datetime

# Practice Question # 1
#
# Import the built-in "datetime" module.
#
# Store the current date and time
# using the appropriate method
# in a variable named "current_datetime".
#
# Print:
#
# 1. The current date and time.
# 2. Its data type.
#
# Expected Output:
#
# 2026-07-30 10:45:12.345678
#
# <class 'datetime.datetime'>
#
# (The actual date and time will be different.)


current_datetime = datetime.datetime.now()

print(current_datetime)

print(type(current_datetime))



# Practice Question # 2
#
# Import the built-in "datetime" module.
#
# Store the current date and time
# using the "today()" method
# in a variable named "current_date".
#
# Print:
#
# 1. The current date and time.
# 2. Its data type.
#
# Expected Output:
#
# 2026-07-30 11:32:45.123456
#
# <class 'datetime.datetime'>
#
# (The actual date and time will be different.)

current_date = datetime.datetime.today()

print(current_date)

print(type(current_date))


# Practice Question # 3
#
# Import the built-in "datetime" module.
#
# Store the current date and time
# in a variable named "current_date_time".
#
# Then:
#
# 1. Store only the date in a variable named "current_date".
# 2. Store only the time in a variable named "current_time".
#
# Print:
#
# 1. The current date.
# 2. Its data type.
#
# 3. The current time.
# 4. Its data type.
#
# Expected Output:
#
# 2026-07-30
# <class 'datetime.date'>
#
# 11:45:18.456789
# <class 'datetime.time'>
#
# (The actual values will be different.)


current_date_time = datetime.datetime.now()

current_date = datetime.datetime.date(current_date_time)

current_time = datetime.datetime.time(current_date_time)

print(current_date)
print(type(current_date))

print(current_time)
print(type(current_time))

# There is another way to do it.

current_date_1 = current_date_time.date()

current_time_1 = current_date_time.time()

print(current_date_1)

print(current_time_1)



# Practice Question # 4
#
# Import the built-in "datetime" module.
#
# Store the current date and time
# in a variable named "current_datetime".
#
# Create the following variables:
#
# year
# month
# day
# hour
# minute
# second
#
# Print each value.
#
# Then print the data type of each variable.
#
# Expected Output:
#
# 2026
# <class 'int'>
#
# 7
# <class 'int'>
#
# 30
# <class 'int'>
#
# 11
# <class 'int'>
#
# 45
# <class 'int'>
#
# 18
# <class 'int'>
#
# (The actual values will be different.)


current_datetime = datetime.datetime.today()

year = current_datetime.year
print(year)
print(type(year))

month = current_datetime.month
print(month)
print(type(month))

day = current_datetime.day
print(day)
print(type(day))

hour = current_datetime.hour
print(hour)
print(type(hour))

minute = current_datetime.minute
print(minute)
print(type(minute))

second = current_datetime.second
print(second)
print(type(second))



# Practice Question # 5
#
# Import the built-in "datetime" module.
#
# Create a datetime object named "meeting".
#
# Meeting details:
#
# Year   : 2026
# Month  : 12
# Day    : 25
# Hour   : 10
# Minute : 30
# Second : 15
#
# Print:
#
# 1. The datetime object.
# 2. Its data type.
#
# Expected Output:
#
# 2026-12-25 10:30:15
#
# <class 'datetime.datetime'>

meeting = datetime.datetime(2026, 12, 25, 10, 30, 15)

print(meeting)

print(type(meeting))


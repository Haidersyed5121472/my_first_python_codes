import datetime

# Practice Question # 1
#
# Import the built-in "datetime" module.
#
# Create a datetime object named "meeting"
# with the following values:
#
# Year   : 2026
# Month  : 12
# Day    : 25
# Hour   : 10
# Minute : 30
# Second : 15
#
# Using strftime(),
# store only the year
# in a variable named "year".
#
# Print:
#
# 1. The year.
# 2. Its data type.
#
# Expected Output:
#
# 2026
#
# <class 'str'>

meeting = datetime.datetime(2026, 12, 25, 10, 30, 15)

year = meeting.strftime("%Y")

print(year)
print(type(year))


# Practice Question # 2
#
# Import the built-in "datetime" module.
#
# Create a datetime object named "meeting"
# with the following values:
#
# Year   : 2026
# Month  : 12
# Day    : 25
# Hour   : 10
# Minute : 30
# Second : 15
#
# Using strftime(),
# store only the month
# in a variable named "month".
#
# Print:
#
# 1. The month.
# 2. Its data type.
#
# Expected Output:
#
# 12
#
# <class 'str'>

meeting_1 = datetime.datetime(2026, 12, 25, 10, 30, 15)

month = meeting_1.strftime("%m")

print(month)
print(type(month))


# Practice Question # 3
#
# Import the built-in "datetime" module.
#
# Create a datetime object named "meeting"
# with the following values:
#
# Year   : 2026
# Month  : 12
# Day    : 25
# Hour   : 10
# Minute : 30
# Second : 15
#
# Using strftime(),
# store only the day
# in a variable named "day".
#
# Print:
#
# 1. The day.
# 2. Its data type.
#
# Expected Output:
#
# 25
#
# <class 'str'>


meeting_2 = datetime.datetime(2026, 12, 25, 10, 30, 15)

day = meeting_2.strftime("%d")

print(day)
print(type(day))


# strftime() - Practice Question # 4
#
# Import the built-in "datetime" module.
#
# Create a datetime object named "meeting"
# with the following values:
#
# Year   : 2026
# Month  : 12
# Day    : 25
# Hour   : 10
# Minute : 30
# Second : 15
#
# Using strftime(), create the following variables:
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
# 12
# 25
# 10
# 30
# 15
#
# <class 'str'> for every variable.

meeting_3 = datetime.datetime(2026, 12, 25, 10, 30, 15)

year = meeting_3.strftime("%Y")
month = meeting_3.strftime("%m")
day = meeting_3.strftime("%d")
hour = meeting_3.strftime("%H")
minute = meeting_3.strftime("%M")
second = meeting_3.strftime("%S")

print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)

print(type(year), type(month), type(day), type(hour), type(minute), type(second))


# Practice Question # 5
#
# Import the built-in "datetime" module.
#
# Create a datetime object named "meeting"
# with the following values:
#
# Year   : 2026
# Month  : 12
# Day    : 25
# Hour   : 10
# Minute : 30
# Second : 15
#
# Using strftime(),
# create the following variables:
#
# full_day_name
# short_day_name
#
# Print:
#
# 1. The full day name.
# 2. Its data type.
#
# 3. The short day name.
# 4. Its data type.
#
# Expected Output:
#
# Friday
# <class 'str'>
#
# Fri
# <class 'str'>

meeting_4 = datetime.datetime(2026, 12, 25, 10, 30, 15)

full_day_name = meeting_4.strftime("%A")
short_day_name = meeting_4.strftime("%a")

print(full_day_name)
print(type(full_day_name))

print(short_day_name)
print(type(short_day_name))


# Practice Question # 6
#
# Import the built-in "datetime" module.
#
# Create a datetime object named "meeting"
# with the following values:
#
# Year   : 2026
# Month  : 12
# Day    : 25
# Hour   : 10
# Minute : 30
# Second : 15
#
# Using strftime(),
# create the following variables:
#
# full_month_name
# short_month_name
#
# Print:
#
# 1. The full month name.
# 2. Its data type.
#
# 3. The short month name.
# 4. Its data type.
#
# Expected Output:
#
# December
# <class 'str'>
#
# Dec
# <class 'str'>


meeting_5 = datetime.datetime(2026, 12, 25, 10, 30, 15)

full_month_name = meeting_5.strftime("%B")
short_month_name = meeting_5.strftime("%b")

print(full_month_name)
print(type(full_month_name))

print(short_month_name)
print(type(short_month_name))


# Practice Question # 7
#
# Import the built-in "datetime" module.
#
# Create a datetime object named "meeting"
# with the following values:
#
# Year   : 2026
# Month  : 12
# Day    : 25
# Hour   : 10
# Minute : 30
# Second : 15
#
# Using strftime(),
# create the following variables:
#
# time_12_hour
# am_pm
#
# Print:
#
# 1. The time in 12-hour format.
# 2. The AM/PM indicator.
#
# Expected Output:
#
# 10
# AM


meeting_6 = datetime.datetime(2026, 12, 25, 10, 30, 15)

time_12_hour = meeting_6.strftime("%I")
am_pm = meeting_6.strftime("%p")

print(time_12_hour)
print(type(time_12_hour))

print(am_pm)
print(type(am_pm))


# Practice Question # 8
#
# Import the built-in "datetime" module.
#
# Create a datetime object named "meeting"
# with the following values:
#
# Year   : 2026
# Month  : 12
# Day    : 25
# Hour   : 10
# Minute : 30
# Second : 15
#
# Using ONE strftime() call,
# create a variable named "formatted_date"
# with the following output:
#
# Friday, 25 December 2026 - 10:30 AM
#
# Print:
#
# 1. The formatted date.
# 2. Its data type.
#
# Expected Output:
#
# Friday, 25 December 2026 - 10:30 AM
#
# <class 'str'>


meeting_7 = datetime.datetime(2026, 12, 25, 10, 30, 15)

formatted_date = meeting_7.strftime("%A, %d %B %Y - %H:%M %p")


print(formatted_date)
print(type(formatted_date))






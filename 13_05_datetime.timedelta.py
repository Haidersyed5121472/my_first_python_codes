import datetime

# Practice Question # 1
#
# Import the built-in "datetime" module.
#
# Store the current date and time
# in a variable named "current_datetime".
#
# Create a timedelta object
# representing 7 days
# and store it in a variable named "seven_days".
#
# Add the timedelta to the current date and time
# and store the result
# in a variable named "future_date".
#
# Print:
#
# 1. The current date and time.
# 2. The future date and time (after 7 days).
#
# Expected Output:
#
# Current:
# 2026-07-30 16:45:10.123456
#
# Future:
# 2026-08-06 16:45:10.123456
#
# (The actual values will be different.)

current_datetime = datetime.datetime.now()

seven_days = datetime.timedelta(days=7)

future_date = current_datetime + seven_days

print(current_datetime)
print(future_date)


# Practice Question # 2
#
# Import the built-in "datetime" module.
#
# Store the current date and time
# in a variable named "current_datetime_1".
#
# Create a timedelta object
# representing 30 days
# and store it in a variable named "thirty_days".
#
# Subtract the timedelta
# from the current date and time
# and store the result
# in a variable named "past_date".
#
# Print:
#
# 1. The current date and time.
# 2. The past date and time (30 days earlier).
#
# Expected Output:
#
# Current:
# 2026-07-30 17:45:10.123456
#
# Past:
# 2026-06-30 17:45:10.123456
#
# (The actual values will be different.)

current_datetime_1 = datetime.datetime.now()

thirty_days = datetime.timedelta(days=30)

past_date = current_datetime_1 - thirty_days

print(current_datetime_1)
print(past_date)


# Practice Question # 3
#
# Import the built-in "datetime" module.
#
# Create two datetime objects:
#
# start_date
# Year   : 2026
# Month  : 7
# Day    : 1
#
# end_date
# Year   : 2026
# Month  : 7
# Day    : 30
#
# Subtract start_date from end_date
# and store the result
# in a variable named "difference".
#
# Print:
#
# 1. The difference.
# 2. Its data type.
#
# Expected Output:
#
# 29 days, 0:00:00
#
# <class 'datetime.timedelta'>

start_date = datetime.datetime(2026, 7, 1)

end_date = datetime.datetime(2026, 7, 30)

difference = end_date - start_date

print(difference)

print(type(difference))


# Practice Question # 4
#
# Import the built-in "datetime" module.
#
# Create two datetime objects:
#
# joining_date
# Year   : 2026
# Month  : 1
# Day    : 10
#
# current_date
# Year   : 2026
# Month  : 7
# Day    : 30
#
# Subtract joining_date from current_date
# and store the result
# in a variable named "experience".
#
# Using the appropriate attribute,
# store only the total number of days
# in a variable named "total_days".
#
# Print:
#
# 1. The timedelta object.
# 2. The total number of days.
# 3. The data type of total_days.
#
# Expected Output:
#
# 201 days, 0:00:00
#
# 201
#
# <class 'int'>

joining_date = datetime.datetime(2026, 1, 10)

current_date = datetime.datetime(2026, 7, 30)

experience = current_date - joining_date

total_days = experience.days

print(experience)
print(total_days)
print(type(total_days))


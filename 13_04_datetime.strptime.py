import datetime

# Practice Question # 1
#
# Import the built-in "datetime" module.
#
# Create a string variable named "date"
# with the following value:
#
# "25/12/2026"
#
# Using strptime(),
# convert the string into a datetime object
# and store it in a variable named "date_object".
#
# Print:
#
# 1. The datetime object.
# 2. Its data type.
#
# Expected Output:
#
# 2026-12-25 00:00:00
#
# <class 'datetime.datetime'>

date = "25/12/2026"

date_object = datetime.datetime.strptime(date, "%d/%m/%Y")

print(date_object)
print(type(date_object))


# Practice Question # 2
#
# Import the built-in "datetime" module.
#
# Create a string variable named "date_1"
# with the following value:
#
# "30-07-2026"
#
# Using strptime(),
# convert the string into a datetime object
# and store it in a variable named "date_1_object".
#
# Print:
#
# 1. The datetime object.
# 2. Its data type.
#
# Expected Output:
#
# 2026-07-30 00:00:00
#
# <class 'datetime.datetime'>

date_1 = "30-07-2026"

date_1_object = datetime.datetime.strptime(date_1, "%d-%m-%Y")

print(date_1_object)
print(type(date_1_object))


# Practice Question # 3
#
# Import the built-in "datetime" module.
#
# Create a string variable named "date_2"
# with the following value:
#
# "25 December 2026"
#
# Using strptime(),
# convert the string into a datetime object
# and store it in a variable named "date_2_object".
#
# Print:
#
# 1. The datetime object.
# 2. Its data type.
#
# Expected Output:
#
# 2026-12-25 00:00:00
#
# <class 'datetime.datetime'>

date_2 = "25 December 2026"

date_2_object = datetime.datetime.strptime(date_2, "%d %B %Y")

print(date_2_object)
print(type(date_2_object))


# Practice Question # 4
#
# Import the built-in "datetime" module.
#
# Create a string variable named "date_3"
# with the following value:
#
# "25 Dec 2026"
#
# Using strptime(),
# convert the string into a datetime object
# and store it in a variable named "date_3_object".
#
# Print:
#
# 1. The datetime object.
# 2. Its data type.
#
# Expected Output:
#
# 2026-12-25 00:00:00
#
# <class 'datetime.datetime'>

date_3 = "25 Dec 2026"

date_3_object = datetime.datetime.strptime(date_3, "%d %b %Y")

print(date_3_object)
print(type(date_3_object))


# Practice Question # 5
#
# Import the built-in "datetime" module.
#
# Create a string variable named "meeting"
# with the following value:
#
# "25/12/2026 10:30 PM"
#
# Using strptime(),
# convert the string into a datetime object
# and store it in a variable named "meeting_object".
#
# Print:
#
# 1. The datetime object.
# 2. Its data type.
#
# Expected Output:
#
# 2026-12-25 22:30:00
#
# <class 'datetime.datetime'>

meeting = "25/12/2026 10:30 PM"

meeting_object = datetime.datetime.strptime(meeting, "%d/%m/%Y %I:%M %p")

print(meeting_object)
print(type(meeting_object))



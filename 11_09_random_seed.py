import random

# Practice Question #1
#
# Import the built-in "random" module.
#
# Set the random seed to 25.
#
# Then generate three random integers
# between 1 and 50 (both included)
# using the appropriate function.
#
# Store each random integer
# in a separate variable.
#
# Print all three integers.
#
# Expected Output:
#
# 17
# 49
# 1
#
# OR
#
# Any other three integers,
# but the output should remain
# exactly the same every time
# you run the program
# with the same seed value.



random.seed(25)

a1 = random.randint(1, 50)
a2 = random.randint(1, 50)
a3 = random.randint(1, 50)

print(a1)
print(a2)
print(a3)


# Practice Question #2
#
# Import the built-in "random" module.
#
# Set the random seed to 100.
#
# Create a list containing
# the following student names:
#
# Ali
# Ahmed
# Sara
# Fatima
# Bilal
#
# Select one random student
# using the appropriate function.
#
# Print the selected student.
#
# Run the program multiple times.
#
# Observe whether the same student
# is selected every time.
#
# Expected Output:
#
# Ahmed
#
# OR
#
# Sara
#
# OR
#
# Any one student,
# but the same student
# should be selected every time
# you run the program
# with the same seed value.

random.seed(100)

students = ["Ali", "Ahmed", "Sara", "Fatima", "Bilal"]

selection = random.choice(students)

print(selection)




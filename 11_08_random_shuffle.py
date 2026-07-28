import random

# Practice Question #1
#
# Import the built-in "random" module.
#
# Create a list containing
# the following numbers:
#
# 10
# 20
# 30
# 40
# 50
#
# Shuffle the list
# using the appropriate function.
#
# Print:
#
# 1. The shuffled list.
# 2. The data type of the returned object
#    from the shuffle function.
#
# Expected Output:
#
# [40, 10, 50, 20, 30]
#
# None
#
# (The shuffled list will be different each time.)
#
# Hint:
#
# Store the return value of the shuffle function
# in a separate variable before printing it.

lst = [10, 20, 30, 40, 50]

shuffeled_lst = random.shuffle(lst)

a = shuffeled_lst

print(lst)

print(a)

print(type(a))


# Practice Question #2
#
# Import the built-in "random" module.
#
# Create a list containing
# the following quiz questions:
#
# Question 1
# Question 2
# Question 3
# Question 4
# Question 5
#
# Shuffle the list
# using the appropriate function.
#
# Print:
#
# 1. The shuffled list.
#
# Then print only
# the first question
# from the shuffled list.
#
# Expected Output:
#
# ['Question 4', 'Question 2', 'Question 5', 'Question 1', 'Question 3']
#
# First Question:
# Question 4
#
# (The order will be different each time.)

question_lst = ["Question 1", "Question 2", "Question 3", "Question 4", "Question 5", ]

shuffeled_questions = random.shuffle(question_lst)

print(question_lst)

print("First Question :", question_lst[0])



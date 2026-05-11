
# --------------------Loops in Python -----------------


# 1- Write a program to print Multiplication table of a given number using for loop.

n = int(input("Enter the number: "))
for i in range (1, 11):
  print(f"{n}X{i} = { n * i}")

------------------------------------------

# Enter the number: 9
# 9X1 = 9
# 9X2 = 18
# 9X3 = 27
# 9X4 = 36
# 9X5 = 45
# 9X6 = 54
# 9X7 = 63
# 9X8 = 72
# 9X9 = 81
# 9X10 = 90


----------------------------------------------------------------------------------------------------


# 1.1- Multiplication table of decimel number.

n = float(input("Enter the number: "))
for i in range (1, 11):
  print(f"{n}X{i} = {n * i}")

---------------------------------------------------

# Enter the number: 2.5
# 2.5X1 = 2.5
# 2.5X2 = 5.0
# 2.5X3 = 7.5
# 2.5X4 = 10.0
# 2.5X5 = 12.5
# 2.5X6 = 15.0
# 2.5X7 = 17.5
# 2.5X8 = 20.0
# 2.5X9 = 22.5
# 2.5X10 = 25.0


----------------------------------------------------------------------------------------------------


# 2- write a program to greet all the person names stored in a list "l" and which starts with S.
# l = ["Haider", "Syed", "Ali", "Shadab"]

l = ["Haider", "Syed", "Ali", "Shadab"]
for name in l:
  if name.startswith("S"):
    print("Hello", name)

--------------------------------------------------

# Hello Syed
# Hello Shadab


----------------------------------------------------------------------------------------------------


# 3- Attempt problem 1 using while loop.

n = int(input("Enter the number: "))
i = 1
while i < 11:
  print(f"{n}X{i} = {n * i}")
  i += 1

--------------------------------------------------

# Enter the number: 5
# 5X1 = 5
# 5X2 = 10
# 5X3 = 15
# 5X4 = 20
# 5X5 = 25
# 5X6 = 30
# 5X7 = 35
# 5X8 = 40
# 5X9 = 45
# 5X10 = 50


----------------------------------------------------------------------------------------------------


# 4- write a program to find whether a given number is prime or not .

n = int(input("Enter the number: "))
if n < 2:
  print("N/A")
else:
  for i in range (2, n):
    if n%i==0:
      print("Not Prime")
      break
  else:
    print("Prime")

------------------------------------------------------------

# Enter the number: 23
# Prime


----------------------------------------------------------------------------------------------------


# 5- write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the number: "))
i = 1
total = 0
while (i<=n):
  total += i
  i += 1
print(total)

------------------------------------------------------------

# Enter the number: 10
# 55


----------------------------------------------------------------------------------------------------


# 6- write a program to calculate the factorial of a given number using for loop .

n = int(input("Enter the number: "))
product = 1
for i in range (1, n+1):
  product = i * product

print(f"The factorial of {n} is {product}.")

---------------------------------------------------

# Enter the number: 7
# The factorial of 7 is 5040.


----------------------------------------------------------------------------------------------------


# 7- write a program to print the following star pattern.

''' for n = 3
  *
 ***
*****
'''
n = int(input("Enter the number: "))
for i in range (1, n+1):
  print(" " * (n-i) + "*" * (2 * i-1))

----------------------------------------------------

# Enter the number: 5
#    *
#   ***
#  *****
# *******
#*********


----------------------------------------------------------------------------------------------------


# 8- write a program to print the following star pattern.
'''
*
**
*** for n = 3
'''
n = int(input("Enter the number: "))
for i in range (1, n+1):
  print("*" * i)

------------------------------------------------

# Enter the number: 5
# *
# **
# ***
# ****
# *****

----------------------------------------------------------------------------------------------------


# 9- write a program to print the fillowing star pattern.
'''

***
* * for n = 3
***

'''
n = int(input("Enter the number: "))
for i in range (1, n+1):
 if i == 1 or i == n:
   print("*" * n)
 else:
   print("*" + " " * (n-2) + "*")

----------------------------------------------

# Enter the number: 5
# *****
# *   *
# *   *
# *   *
# *****


----------------------------------------------------------------------------------------------------


# 10- write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter the number: "))
for i in range (1, 11):
  print(f"{n}X{11-i} = {n * (11-i)}")

-----------------------------------------------

# Enter the number: 5
# 5X10 = 50
# 5X9 = 45
# 5X8 = 40
# 5X7 = 35
# 5X6 = 30
# 5X5 = 25
# 5X4 = 20
# 5X3 = 15
# 5X2 = 10
# 5X1 = 5


----------------------------------------------------------------------------------------------------


# 11- Write a program to print all numbers from 1 to 20 except multiples of 5 using continue.

for i in range (1, 21):
  if i%5==0:
    continue
  print(i)

-------------------------------------

# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 11
# 12
# 13
# 14
# 16
# 17
# 18
# 19


----------------------------------------------------------------------------------------------------


# 12- Write a program that takes a list of numbers and prints them one by one using for loop,
# but stops the loop when number 0 appears (use break).

l = [5, 2, 11, 19, 35, 0, 55, 12, 15]
for i in l:
  if i == 0:
    break
  print(i)

-----------------------------------------------------

# 5
# 2
# 11
# 19
# 35


----------------------------------------------------------------------------------------------------


# 13- Write a program to print numbers from 1 to 10 using for loop and use pass when number is 5.

for i in range (1, 11):
  if i == 5:
    pass
  print(i)

----------------------------------------------

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


----------------------------------------------------------------------------------------------------


# 14- Write a program to check whether a given number is present in a list or not using in.

l = [5, 2, 11, 19, 35, 0, 55, 12, 15]
num = int(input("Enter the number: "))
if num in l:
  print("Yes")
else:
  print("No")

----------------------------------------------

# Enter the number: 15
# Yes


----------------------------------------------------------------------------------------------------


# 15- Write a program to count total elements in a list without writing the number manually (use len()).

l = ["Haider", True, 5.255, 77, "Ali"]
print(len(l))

--------------------------------------------

# 5


----------------------------------------------------------------------------------------------------


# 16- Write a program to print numbers from 1 to 10 using for loop and use else with the loop to print "Loop Finished".

for i in range (1, 11):
  print(i)
else:
  print("Loop Finished")

---------------------------------

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Loop Finished


----------------------------------------------------------------------------------------------------


# 17- Write a program to print the sum of all elements of a list using sum().

l = [5, 10, 15, 20]
print(sum(l))

-----------------------

# 50


----------------------------------------------------------------------------------------------------


# 18- Write a program to find the maximum and minimum number from a list using max() and min().

l = [5, 2, 11, 19, 35, 0, 55, 12, 15]
print(max(l))
print(min(l))

-----------------------------------------

# 55
# 0


----------------------------------------------------------------------------------------------------


# 19- Write a program to print elements of a list along with their index numbers using enumerate().

l = [5, 2, 11, 19, 35, 0, 55, 12, 15]
for i in enumerate(l):
  print(i)

------------------------------------------

# (0, 5)
# (1, 2)
# (2, 11)
# (3, 19)
# (4, 35)
# (5, 0)
# (6, 55)
# (7, 12)
# (8, 15)


----------------------------------------------------------------------------------------------------


# 20- Write a program to reverse a list using reversed() and print the output using a loop.

l = [5, 2, 11, 19, 35, 0, 55, 12, 15]
for i in reversed(l):
  print(i)

-----------------------------------------

# 15
# 12
# 55
# 0
# 35
# 19
# 11
# 2
# 5


----------------------------------------------------------------------------------------------------


# 21- Write a program to sort a list of numbers and print them one by one using sorted().

l = [5, 2, 11, 19, 35, 0, 55, 12, 15]
for i in sorted(l):
  print(i)

-------------------------------------------

# 0
# 2
# 5
# 11
# 12
# 15
# 19
# 35
# 55


----------------------------------------------------------------------------------------------------


# 22- Write a program to check if any number in a list is greater than 50 using any().

l = [5, 2, 11, 19, 35, 0, 55, 12, 15]
if any(i > 50 for i in l):
  print("Yes at least one number is greater then 50.")
else:
  print("No number is greater then 50.")

----------------------------------------------------------

# Yes at least one number is greater then 50.


----------------------------------------------------------------------------------------------------

# 23- Write a program to check if all numbers in a list are positive using all().

l = [5, 2, 11, -55, 12, 15]
if all(i > 0 for i in l):
  print("All numbers are positive.")
else:
  print("Not all numbers are positive")

---------------------------------------------

# Not all numbers are positive


----------------------------------------------------------------------------------------------------


# 24- Write a program to multiply all numbers of a list by 2 using map() and print the result using a loop.

l = [5, 2, 11, -55, 12, 15]
for i in map(lambda x: x * 2, l):
  print(i)

------------------------------------------------

# 10
# 4
# 22
# -110
# 24
# 30


----------------------------------------------------------------------------------------------------


# 25- Write a program to print only even numbers from a list using filter().

l = [5, 2, 11, -55, 12, 15]
for i in filter(lambda x: x%2==0, l):
  print(i)

-------------------------------------------

# 2
# 12


----------------------------------------------------------------------------------------------------

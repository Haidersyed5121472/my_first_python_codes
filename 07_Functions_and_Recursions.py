7 - [[[[[[[[[[[[[[[[ Functions & Recursions ]]]]]]]]]]]]]]]]]


# 1- Write a program using functions to find greatest of three numbers.

def greatest(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return f"Num 1 {num1} is the greatest number."
  elif num2 >= num1 and num2 >= num3:
    return f"Num 2 {num2} is the greatest number."
  else:
    return f"Num 3 {num3} is the greatest number."

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print(greatest(num1, num2, num3))

--------------------------------------------------------------------------

Enter first number: 55
Enter second number: 22
Enter third number: 56
Num 3 56 is the greatest number.


----------------------------------------------------------------------------------------------------


# 2- Write a python program using function to convert fahrenheit to celsius.


def f_to_c(temp):
  return 5* (temp-32)/9

temp = float(input("Enter temperature in Fahrenheit: "))
a = f_to_c(temp)
print(f"{round(a, 2)}")

----------------------------------------------------------

Enter temperature in Fahrenheit: 100
37.78


----------------------------------------------------------------------------------------------------


# 2.1- Celsius to Fahrenheit

def c_to_f(temp):
  return 9/5 * (temp)+32

temp = float(input("Enter temperature in Celsius: "))
a = c_to_f(temp)
print(f"{round(a, 2)}")

-------------------------------------------------------

Enter temperature in Celsius: 37.78
100.0


----------------------------------------------------------------------------------------------------


# 3- How do you prevent a python print() function to print a new line at the end.

print("a")
print("b")
print("c")

# now we are going to prevent print function to print a new line.

print("a", end="")
print("b", end="")
print("c", end="")

----------------------------------------------------------------

a
b
c
abc


----------------------------------------------------------------------------------------------------


# 4- Write a recursive funtion to calculate the sum of first n natural numbers.

def sum(num):
  if num == 1:
    return 1
  return num + sum(num-1)

num = int(input("Enter a number: "))
print(sum(num))

------------------------------------------

Enter a number: 10
55


----------------------------------------------------------------------------------------------------


# 5- Write a python function to print first n lines of the following pattern:
'''
***
**
*   for n = 3
'''

def pattern(n):
  if n == 0:
    return
  print("*" * n)
  pattern(n-1)

n = int(input("Enter a number: "))
pattern(n)

----------------------------------------------

Enter a number: 3
***
**
*


----------------------------------------------------------------------------------------------------


# 6- Write a python function which converts inches to cms.

def inc_to_cm(inches):
  return inches * 2.54

inches = float(input("Enter inches: "))
a = inc_to_cm(inches)
print(f"{round(a, 2)}")

----------------------------------------------

Enter inches: 10
25.4


----------------------------------------------------------------------------------------------------


# 6.1- cms to inches

def cm_to_inc(cms):
  return cms / 2.54

cms = float(input("Enter Centimeters: "))
a = cm_to_inc(cms)
print(f"{round(a, 2)}")

------------------------------------------

Enter Centimeters: 25.4
10.0


----------------------------------------------------------------------------------------------------


# 7- Write a python function to remove a given word from a list and strip it at a same time.

def rem(l, word):
  for item in l:
    l.remove(word)
    return l

lst = ["Ahmed", "Hameed", "Rasheed","ed"]
print(rem(lst, "ed"))

def rem(l, word):
  lis = []
  for item in l:
    if not (item==word):
      lis.append(item.strip(word))

  return lis

lst = ["Ahmed", "Hameed", "Rasheed","ed"]
print(rem(lst, "ed"))

---------------------------------------------

['Ahmed', 'Hameed', 'Rasheed']
['Ahm', 'Ham', 'Rash']


----------------------------------------------------------------------------------------------------


# 8- Write a python function to print multiplication table of a given number.

def table(n):
  for i in range (1, 11):
    print(f"{n} X {i} = {n * i}")

n = int(input("Enter a number: "))
table(n)

------------------------------------------

Enter a number: 9
9 X 1 = 9
9 X 2 = 18
9 X 3 = 27
9 X 4 = 36
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81
9 X 10 = 90


----------------------------------------------------------------------------------------------------


# 9-
# Write a function which takes two numbers as input
# and returns their sum.
# Store the returned value in a variable and print it.


def plus(n1, n2):
  return n1 + n2

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

a = plus(n1, n2)
print(a)

-----------------------------------------------------

Enter the first number: 5
Enter the second number: 12
17


----------------------------------------------------------------------------------------------------


# 10-
# Write a function which takes name and age as input
# and returns "Eligible" if age is 18 or above,
# otherwise returns "Not Eligible"

def eligibility(name , age):
  if age >= 18:
    return "Eligible"
  else:
    return "Not Eligible"

name = input("Enter the name: ")
age = int(input("Enter the age: "))
print(eligibility(name,age))

-------------------------------------------------------

Enter the name: Haider
Enter the age: 23
Eligible


----------------------------------------------------------------------------------------------------


# 11-
# Write a function which takes a string as input
# and checks:
# - length of the string
# - whether the string is empty or not

def len_of_string(sen):
  length = len(sen)
  if length == 0:
    return f"Length: {length}, String is Empty."
  else:
    return f"Length: {length}, String is not Empty."

sen = input("Enter the String: ")
print(len_of_string(sen))

--------------------------------------------------------

Enter the String: Hello
Length: 5, String is not Empty.


----------------------------------------------------------------------------------------------------


# 12-
# Write a function intro() which takes:
# - name
# - country (default value = "Pakistan")
# The function should print user introduction.
# Call the function once without country
# and once using keyword argument.

def intro(name , country="Pakistan"):
  print(f"My name is {name}. I'm from {country}.")

intro("Haider")
intro("Haider", "Canada")

-----------------------------------------------------

My name is Haider. I'm from Pakistan.
My name is Haider. I'm from Canada.


----------------------------------------------------------------------------------------------------


# 13-
# Write a function which takes three numbers
# but the third number should be optional.
# If third number is not provided,
# return sum of first two numbers only.

def addition(n1, n2, n3=None):
  if n3 is None:
    return n1 + n2
  else:
    return n1 + n2 + n3

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
choice = input("Do you want to enter the third number? (yes/no): ")
if choice.lower() == "yes":
  n3 = int(input("Enter the third number: "))
  print(addition(n1 , n2 , n3))
else:
  print(addition(n1 , n2))

---------------------------------------------------------------------

Enter the first number: 17
Enter the second number: 21
Do you want to enter the third number? (yes/no): yes
Enter the third number: 12
50


----------------------------------------------------------------------------------------------------


# 14-
# Write a function which calculates square of a number
# and returns the value.
# Store the returned value in a variable
# and use it in another calculation.

def calculate_sqr(n):
  return n ** 2

num = int(input("Enter the number: "))
square = calculate_sqr(num)
print(square)
print(square * 2)

---------------------------------------------------------

Enter the number: 3
9
18


----------------------------------------------------------------------------------------------------


# 15-
# Write a function which only prints a message.
# Store the function call in a variable and print it.
# Observe the output and understand why it happens.

def message(a):
  print(a)

a = input("Enter the message: ")
z = message(a)
print(z)

----------------------------------------------------------

Enter the message: Hello Everyone
Hello Everyone
None


----------------------------------------------------------------------------------------------------


# 16-
# Write a function which takes a list as input
# and returns a new list containing only even numbers.

def get_even_numbers(numbers):
  even_number = []
  for i in numbers:
    if i % 2 == 0:
      even_number.append(i)
  return even_number

nums = list(map(int, input("Enter the numbers with space: ").split()))
print(get_even_numbers(nums))

----------------------------------------------------------------------

Enter the numbers with space: 0 3 2 5 8 1 6 9 12
[0, 2, 8, 6, 12]


----------------------------------------------------------------------------------------------------


# 17-
# Write a function which takes a string as input
# and removes extra spaces from it.
# Return the cleaned string.

def clean_string(strn):
  return strn.strip()

a = input("Enter the string: ")
print(clean_string(a))

-----------------------------------------------------

Enter the string:                  Hello How is going your life ?                      
Hello How is going your life ?


----------------------------------------------------------------------------------------------------


# 18-
# Write a recursive function to calculate factorial of a number. 

def fact(num):
  if num==0 or num==1:
    return 1
  return fact(num-1) * num

n = int(input("Enter the number: "))
print(fact(n))

-------------------------------------------------------------------

Enter the number: 6
720


----------------------------------------------------------------------------------------------------


# 19-
# Write a recursive function which prints countdown
# from n to 1.

def count(n):
  if n == 0:
    return
  print(n)
  count(n-1)

n = int(input("Enter the number: "))
count(n)

--------------------------------------------------------

Enter the number: 10
10
9
8
7
6
5
4
3
2
1


----------------------------------------------------------------------------------------------------


# 20-
# Write a recursive function which calculates
# the sum of all numbers present in a list
# without using loops.

def addition(lst):
  if not lst:
    return 0
  return lst[0] + addition(lst[1:])

l = [5, 10, 15, 20]
total = addition(l)
print(total)

------------------------------------------------------

50


----------------------------------------------------------------------------------------------------


# 21-
# Write a function which takes product price as input.
# If price is greater than 5000,
# apply 10% discount.
# Return the final price.

def apply_discount(price):
  if price > 5000:
    discount = price * 0.10
    discounted_price = price - discount
    return discounted_price
  else:
    return price

price = float(input("Enter the price: "))
total_price = apply_discount(price)
print(f"{round(total_price , 2)}")

------------------------------------------------------

Enter the price: 5250
4725.0


----------------------------------------------------------------------------------------------------


# 22-
# Write a function which takes marks (0–100) as input
# and returns grade according to marks.

def get_grade(marks):
  if marks > 100 or marks < 0:
    return "Invalid Marks"
  elif marks >= 90:
    return "Grade A+"
  elif marks >= 80:
    return "Grade A"
  elif marks >= 70:
    return "Grade B"
  elif marks >= 60:
    return "Grade C"
  elif marks >= 50:
    return "Grade D"
  else:
    return "Failed"

marks = int(input("Enter the marks: "))
print(get_grade(marks))

------------------------------------------------------------

Enter the marks: 91
Grade A+


----------------------------------------------------------------------------------------------------
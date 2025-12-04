Variables and Data Types

#01

a = 1 #Write a python program to add to numbers.
b = 2

print(a + b)
------------------------------------------------------
3

-------------------------------------------------------------------------------------------------------------------

#02

#write a python program to find remainder when number is divided by z.

a = 34 

b = 5

print("Remainder when a is divided by b is ", a % b)
------------------------------------------------------------------------------
Remainder when a is divided by b is  4


-------------------------------------------------------------------------------------------------------------------

#03

#check the type of variable assigned using input() function.

a = input("Enter the value of a: ") 
print(type(a))
----------------------------------------------------------------
Enter the value of a: 34.2356
<class 'str'>


-------------------------------------------------------------------------------------------------------------------

#04

#use comparison operator to find out weather a given variable 'a' is greater then 'b' or not. take a=34 and b=80

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

print("a is greater then b", a>b)
-------------------------------------------------------------------------------------------------------------
Enter Number 1: 34
Enter Number 2: 80
a is greater then b False


-------------------------------------------------------------------------------------------------------------------

#05

#write a python program to find an avrage of two numbers entered by user.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("The average of these two number is", (a+b)/2)
------------------------------------------------------------------------------
Enter number 1: 125
Enter number 2: 185
The average of these two number is 155.0


-------------------------------------------------------------------------------------------------------------------

#06

#write a python program to calculate a square of a number entered by user.

a = int(input("Enter your number : "))

print("The square of the number is", a**2)
print("The square of the number is", a*a)
----------------------------------------------------------------------------
Enter your number : 7
The square of the number is 49
The square of the number is 49


-------------------------------------------------------------------------------------------------------------------

#07

# user say ek float number input lo aur uska cube  print kro.

num = float(input("Enter a float number: "))
cube = num ** 3
print("The cube of the number is:", cube)
print(f"The cube of {num} is {cube}")
----------------------------------------------------------------
Enter a float number: 2.5
The cube of the number is: 15.625
The cube of 2.5 is 15.625


-------------------------------------------------------------------------------------------------------------------

#08

# user say age input lo aur check kro kya wo 18 say ziada ha ya nahin.
# agar yes ha tou print kro (You are an adult) or agr ans no ha tou print kro (You are underage)

age = int(input("Enter your age: "))
if age >= 18:
  print("You are an adult.")
else:
  print("You are underage.")
---------------------------------------------
Enter your age: 33
You are an adult.


-------------------------------------------------------------------------------------------------------------------

# 09

# List practice: Ek list banao jisme 5 fruits ho. 3rd fruit print kro. list ky end me new fruit add kro or updated list print kro.

fruits = ["Mango", "Orange", "Grapes", "Apple","Banana"]
print(fruits)
print(fruits[3])

new_fruit = input("Enter a new fruit to add: ")
fruits.append(new_fruit)
print(fruits)
--------------------------------------------------------------
['Mango', 'Orange', 'Grapes', 'Apple', 'Banana']
Apple
Enter a new fruit to add: cherry
['Mango', 'Orange', 'Grapes', 'Apple', 'Banana', 'cherry']


-------------------------------------------------------------------------------------------------------------------

# 10

# Ek tuple banao jisme 4 numbers hn aur unka sum print kro.

numbers = (5, 7, 8, 12)
print(numbers)
total = sum(numbers)
print(total)
print(f"The sum of numbers in the tuple is: {total}")
----------------------------------------------------------------
(5, 7, 8, 12)
32
The sum of numbers in the tuple is: 32

-------------------------------------------------------------------------------------------------------------------


# 11

# user say input lo: name, age, city. inhain ek dictionary main store kro or puri dictionary print kro.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("ENter your city: ")

person = {
    "name": name,
    "age": age,
    "city": city,
}

print("Person details dictionary", person)
-------------------------------------------------
Enter your name: Hadi
Enter your age: 33
ENter your city: Rawalpindi
Person details dictionary {'name': 'Hadi', 'age': 33, 'city': 'Rawalpindi'}


-------------------------------------------------------------------------------------------------------------------



# 12

# Ek set banao jisme kuch duplicate numbers hon example{1, 3, 4, 7, 4} set print kro or dakho duplicate remove hua ya nahin.

numbers = {2, 3, 5, 3, 7, 2, 5}
print(numbers)
--------------------------------
{2, 3, 5, 7}

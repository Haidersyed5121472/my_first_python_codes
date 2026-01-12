05- Conditional Expressions

# 1- Write a program to find the greatest of four numbers entered by the user.

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))

if n1>n2 and n1>n3 and n1>n4:
  print("The Greatest Number is n1", n1)
elif n2>n1 and n2>n3 and n2>n4:
  print("The Greatest Number is n2", n2)
elif n3>n1 and n3>n2 and n3>n4:
  print("The Greatest Number is n3", n3)
else:
  print("The Greatest Number is n4", n4)

------------------------------------------------------------------------------------

Enter number 1: 525
Enter number 2: 725
Enter number 3: 786
Enter number 4: 929
The Greatest Number is n4 929

---------------------------------------------------------------------------------------------------------


# I wrote this code to make sure that if two or more numbers are the same, the output is correct.
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))

if n1>=n2 and n1>=n3 and n1>=n4:
  print("The Greatest Number is", n1)
elif n2>=n1 and n2>=n3 and n2>=n4:
  print("The Greatest Number is", n2)
elif n3>=n1 and n3>=n2 and n3>=n4:
  print("The Greatest Number is", n3)
else:
  print("The Greatest Number is ", n4)

-----------------------------------------------------------

Enter number 1: 155
Enter number 2: 125
Enter number 3: 155
Enter number 4: 100
The Greatest Number is 155

---------------------------------------------------------------------------------------------------------

# 2- Write a program to find out whether a student has passed or failed if it requires a total of 40% and
# atleast 33% in each subject to pass. assume 3 subjects and take marks as an input from the user.

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

total_percentage = (100 * (m1+m2+m3)) / 300
if total_percentage>=40 and m1>= 33 and m2>= 33 and m3>= 33:
  print("You have Passed", total_percentage)
else:
  print("You have Failed", total_percentage)

---------------------------------------------------------------------

Enter marks of subject 1: 75
Enter marks of subject 2: 40
Enter marks of subject 3: 40
You have Passed 51.666666666666664

---------------------------------------------------------------------------------------------------------

# 3- A spam comment is defined as a text containing following keywords
# "make a lot of money", "buy now", "subscribe this", "click this". write a program to detect these spams.

c1 = "make a lot of money".lower()
c2 = "buy now".lower()
c3 = "subscribe this".lower()
c4 = "click this".lower()

comment = input("Enter a comment to check if it's spam or not: ").lower()

if c1 in comment or c2 in comment or c3 in comment or c4 in comment:
  print("Spam Comment")
else:
  print("Comment is not spam")

-------------------------------------------------------------------------------

Enter a comment to check if it's spam or not: buy now to get 50% off
Spam Comment

---------------------------------------------------------------------------------------------------------

# 4- Write a program to find whether a given username contains less than 10 characters or not.

u = input("Enter a username: ")

if (len(u)<10):
  print("Username contains less than 10 characters")
else:
  print("Username contains more than 10 characters")

----------------------------------------------------------

Enter a username: asdfasd12
Username contains less than 10 characters

---------------------------------------------------------------------------------------------------------

# 5- Write a program which finds out whether a given name is present in the list or not.

l = ["Haider", "Ali", "Ahmed", "Turab"]
n = input("Enter a name to check if that name is present in a list or not: ")

if n.title() in l:
  print("Given name is present in a list")
else:
  print("Given name is not present in a list")

----------------------------------------------------------

Enter a name to check if that name is present in a list or not: ahmed
Given name is present in a list

---------------------------------------------------------------------------------------------------------

# 6- Write a program to calculate the grade of a student from his marks from the following scheme.
# 90-100 => Ex
# 80-90 => A
# 70-80 => B
# 60-70 => C
# 50-60 => D
# <50   => F


marks = int(input("Enter your marks: "))

if marks<0 or marks>100:
  print("Invalid Marks")
elif marks>=90:
  print("Grade = EX")
elif marks>=80:
  print("Grade = A")
elif marks>=70:
  print("Grade = B")
elif marks>=60:
  print("Grade = C")
elif marks>=50:
  print("Grade = D")
else:
  print("Grade = F")

------------------------------------------------------

Enter your marks: 89
Grade = A

---------------------------------------------------------------------------------------------------------

# 7- Write a program to find out whether a given post is talking about "Harry" or not.

post = input("Enter a post: ").lower()
name = input("Enter a name: ").lower()

if name in post:
  print("This post is talking about", name)
else:
  print("This post is not talking about", name)

--------------------------------------------------------

Enter a post: Harry is going to meet his friends in city centre.
Enter a name: harry
This post is talking about harry

---------------------------------------------------------------------------------------------------------

# 8- User se aik number lo aur check karo:
# - number positive hai
# - negative hai
# - ya zero hai

num = int(input("Enter your number: "))
if num > 0:
  print("Number is Positive")
elif num < 0:
  print("Number is Negative")
else:
  print("Number is Zero")

----------------------------------------------------

Enter your number: -1
Number is Negative

---------------------------------------------------------------------------------------------------------

# 9- User se do numbers lo aur batao:
# - dono equal hain
# - ya kaunsa number bara hai

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > num2:
  print("Number 1 is greater than number 2")
elif num2 > num1:
  print("Number 2 is greater than number 1")
else:
  print("Both numbers are equal")

----------------------------------------------------

Enter number 1: 11
Enter number 2: 11
Both numbers are equal

---------------------------------------------------------------------------------------------------------

# 10- User se aik number lo aur check karo:
# - kya wo even hai AND positive hai

n = int(input("Enter your number: "))

if n>0 and n%2==0:
  print("Number is Even and Positive")
else:
  print("Number is odd or negative")

----------------------------------------------------

Enter your number: 5
Number is odd or negative

---------------------------------------------------------------------------------------------------------

# 11-
# User se aik age lo aur check karo:
# - age 18 se kam hai OR
# - age 60 se zyada hai
# Print karo: "Special category" warna "Normal category"

age = int(input("Enter your age: "))

if age>60 or age<18:
  print("Special Category")
else:
  print("Normal Category")

------------------------------------------------------------

Enter your age: 18
Normal Category

---------------------------------------------------------------------------------------------------------

# 12-
# User se aik number lo aur `not` operator use karke batao:
# - number 10 se chhota nahin hai

n = int(input("Enter your number: "))
if not(n<10):
  print("Number is not less than 10")
else:
  print("Number is less than 10")

------------------------------------------------------------------

Enter your number: 11
Number is not less than 10

---------------------------------------------------------------------------------------------------------

# 13-
# User se username lo aur check karo:
# - username khali (empty) tou nahi

u = input("Enter your username: ")
if (len(u)>0):
  print("Username is not empty")
else:
  print("Username is empty")

--------------------------------------------

Enter your username: asdfadsf123456
Username is not empty

---------------------------------------------------------------------------------------------------------

# 14-
# User se aik password lo aur check karo:
# - length kam az kam 8 characters ho
# - warna print karo "Weak password"

p = input("Enter a password: ")
if (len(p)>=8):
  print("Strong Password")
else:
  print("Weak Password")

-------------------------------------------------

Enter a password: asdf1234
Strong Password

---------------------------------------------------------------------------------------------------------

# 15-
# User se 3 numbers lo aur check karo:
# - kya koi bhi number negative hai (use or)

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

if n1<0 or n2<0 or n3<0:
  print("One of the numbers is negative")
else:
  print("All numbers are positive")

------------------------------------------------------

Enter number 1: 12
Enter number 2: 14
Enter number 3: -5
One of the numbers is negative

---------------------------------------------------------------------------------------------------------

# 16-
# User se 3 numbers lo aur check karo:
# - kya teeno numbers positive hain (use and)

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

if n1>0 and n2>0 and n3>0:
  print("All numbers are positive")
else:
  print("One of the numbers is negative")

-------------------------------------------------------

Enter number 1: 5
Enter number 2: 1
Enter number 3: 2
All numbers are positive

---------------------------------------------------------------------------------------------------------

# 17-
# User se aik number lo aur check karo:
# - number 5 aur 10 ke darmiyan hai (5 aur 10 included)

n = int(input("Enter your number: "))

if n>=5 and n<=10:
  print("Given Condition Met")
else:
  print("Given Condition Not Met")

------------------------------------------------------------------

Enter your number: 11
Given Condation Not Met

---------------------------------------------------------------------------------------------------------

# 18-
# User se aik sentence lo aur check karo:
# - kya is mein word "free" ya "offer" mojood hai (use or + in)

s = input("Enter a sentence: ").lower()

if "free" in s or "offer" in s:
  print("Given Condition met")
else:
  print("Given condition not met")

----------------------------------------------------------------------

Enter a sentence: Is this free of cost ?
Given Condition met

---------------------------------------------------------------------------------------------------------

# 19-
# User se marks lo aur check karo:
# - marks 0–100 ke darmiyan nahi hain (use not)

marks = int(input("Enter your marks: "))

if not(marks>=0 and marks<=100):
  print("Marks are out of range")
else:
  print("Marks are within range")

-----------------------------------------------------------------

Enter your marks: 101
Marks are out of range

---------------------------------------------------------------------------------------------------------

# 20-
# User se aik boolean input lo:
# - agar True hai tou print karo "Access granted"
# - warna "Access denied"

b = input("Enter a boolean: ").lower()

if b == "True".lower():
  print("Access Granted")
else:
  print("Access Denied")

------------------------------------------------------------

Enter a boolean: false
Access Denied

---------------------------------------------------------------------------------------------------------

# 21-
# User se aik number lo aur multiple independent if use karke check karo:
# - agar number even hai tou print karo "Even"
# - agar number positive hai tou print karo "Positive"
# (dono ek sath bhi print ho sakte hain)


n = int(input("Enter your number: "))

if n%2==0:
  print("Number is Even")
else:
  print("Number is Odd")
if n>0:
  print("Number is Positive")
else:
  print("Number is Negative")

------------------------------------------------------------------------------------

Enter your number: -12
Number is Even
Number is Negative

---------------------------------------------------------------------------------------------------------

# This code is strictly according to question number 21

n = int(input("Enter your number: "))

if n%2==0:
  print("Even")
if n>0:
  print("Positive")

----------------------------------------------------

Enter your number: 6
Even
Positive

---------------------------------------------------------------------------------------------------------
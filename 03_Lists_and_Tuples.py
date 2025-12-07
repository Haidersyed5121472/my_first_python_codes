1- Write a program to store seven fruits in a list entered by the user.

fruits = []

f1 = input("Enter fruit name: ")
fruits.append(f1)
f2 = input("Enter fruit name: ")
fruits.append(f2)
f3 = input("Enter fruit name: ")
fruits.append(f3)
f4 = input("Enter fruit name: ")
fruits.append(f4)
f5 = input("Enter fruit name: ")
fruits.append(f5)
f6 = input("Enter fruit name: ")
fruits.append(f6)
f7 = input("Enter fruit name: ")
fruits.append(f7)

print(fruits)
----------------------------------------
Enter fruit name: Banana
Enter fruit name: Orange
Enter fruit name: Guava
Enter fruit name: Kiwi
Enter fruit name: Peach
Enter fruit name: Apple
Enter fruit name: Pine
['Banana', 'Orange', 'Guava', 'Kiwi', 'Peach', 'Apple', 'Pine']


-------------------------------------------------------------------------------------------------------------------

2- Write a program to accept marks of 6 students and Display them in a sorted manner.


marks = []

f1 = int(input("Enter marks here: "))
marks.append(f1)
f2 = int(input("Enter marks here: "))
marks.append(f2)
f3 = int(input("Enter marks here: "))
marks.append(f3)
f4 = int(input("Enter marks here: "))
marks.append(f4)
f5 = int(input("Enter marks here: "))
marks.append(f5)
f6 = int(input("Enter marks here: "))
marks.append(f6)

marks.sort()
print(marks)
------------------------------------------
Enter marks here: 45
Enter marks here: 33
Enter marks here: 52
Enter marks here: 100
Enter marks here: 79
Enter marks here: 25
[25, 33, 45, 52, 79, 100]


-------------------------------------------------------------------------------------------------------------------

3- Check that Tuple type cannot be changed in python.

a = (34, 564, 5.456, "Harry", 55)
a[2] = "Larry"

#tuples is immuatble mean can't be changed.
---------------------------------------------
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipython-input-2951310649.py in <cell line: 0>()
      1 a = (34, 564, 5.456, "Harry", 55)
----> 2 a[2] = "Larry"
      3 
      4 #tuples is immuatble mean can't be changed.

TypeError: 'tuple' object does not support item assignment


-------------------------------------------------------------------------------------------------------------------

4- Write a program to sum a list with 4 numbers.

a = [1, 3, 9, 15]

print(sum(a))
--------------------------------------------------
28



-------------------------------------------------------------------------------------------------------------------


5- Write a program to count the number of zeros in the folowing tuple.
  a = (7, 0, 8, 0, 0, 9)

a = (7, 0, 8, 0, 0, 9)

n = a.count(0)
print(n)
-----------------------------
3

-------------------------------------------------------------------------------------------------------------------



# 6- append() 
# EK program likho jo user se 3 fruits le aur unhain ek empty list main append() karke print kare.

fruits = []

fruit1 = input("Enter fruit 1 name: ")
fruit2 = input("Enter fruit 2 name: ")
fruit3 = input("Enter fruit 3 name: ")

fruits.append(fruit1)
fruits.append(fruit2)
fruits.append(fruit3)

print("Your Fruits list", fruits)
------------------------------------------------------
Enter fruit 1 name: Banana
Enter fruit 2 name: Mango
Enter fruit 3 name: Cherry
Your Fruits list ['Banana', 'Mango', 'Cherry']


-------------------------------------------------------------------------------------------------------------------


# 7- insert() 
#  Ek list = ["apple", "banana", "cherry"] lo, user se ek fruit aur ek position lo aur 
#  us position per insert() krke updated list print kro.


list = ["apple", "banana", "cherry"]

fruit = input("Enter a new fruit: ")
position = int(input("Enter the position to insert the new fruit: "))

list.insert(position, fruit)

print("Updated list", list)
---------------------------------------------------------------------------
Enter a new fruit: Guava
Enter the position to insert the new fruit: 1
Updated list ['apple', 'Guava', 'banana', 'cherry']



-------------------------------------------------------------------------------------------------------------------



# 8- remove()
#    ek list = ["apple", "banana", "cherry", "banana"] list say banana remove kro or updated list print kro.

list = ["apple", "banana", "cherry", "banana"]

list.remove("banana")

print("updated list", list)
----------------------------------------------------------------
updated list ['apple', 'cherry', 'banana']


-------------------------------------------------------------------------------------------------------------------



# 9- pop()
#    ek list [10, 20, 30, 40, 50] index 2 ka element remove krke print kro aur updated list print kro.

list = [10, 20, 30, 40, 50]

list.pop(2)

print("updated", list)
---------------------------------------------
updated [10, 20, 40, 50]



-------------------------------------------------------------------------------------------------------------------



# 10- clear()
# Ek list = [1, 2, 3, 4] list ko clear() krky print kro.

list = [1, 2, 3, 4]

list.clear()

print(list)
------------------------------------------------------------
[]



-------------------------------------------------------------------------------------------------------------------



# 11- reverse()
#  Ek list = [1, 2, 3, 4, 5] list ko ulta (reverse()) krky print kro.

list = [1, 2, 3, 4, 5]

list.reverse()

print(list)
----------------------------------------------------------
[5, 4, 3, 2, 1]


-------------------------------------------------------------------------------------------------------------------


# 12- count() 
#   Ek list = [2, 4, 2, 8, 2, 9] count() method use kr ky check kro 2 kitni br aya ha. 

list = [2, 4, 2, 8, 2, 9]

count = list.count(2)

print(count)
--------------------------------------------
3


-------------------------------------------------------------------------------------------------------------------


# 13- index()
# Ek list = ["Ali", "Farhan", "Hammad"] index() ka use kr ky "Farhan" ka index number print kro.

list = ["Ali", "Farhan", "Hammad"]

index = list.index("Farhan")

print(index)
----------------------------------------------
1



-------------------------------------------------------------------------------------------------------------------


# 14- copy()
# Ek list = (1, 2, 3) copy() method se aik nai list bnao or dono list ko print kro.

list = [1, 2, 3]

new_list = list.copy()

print(list)
print(new_list)
---------------------------------------------
[1, 2, 3]
[1, 2, 3]



-------------------------------------------------------------------------------------------------------------------



# 15- sort()
# Ek list = [9, 1, 7, 2, 5] sort() Method use krky ascending aur descending dono order main print kro.

list = [9, 1, 7, 2, 5]

list.sort()
print("Ascending order", list)

list.sort(reverse=True)
print("Descending order", list)
---------------------------------------------
Ascending order [1, 2, 5, 7, 9]
Descending order [9, 7, 5, 2, 1]



-------------------------------------------------------------------------------------------------------------------



# 16- Tuple - count()
# Ek tuple = (1, 3, 3, 5, 3, 7) count kro kitni dafa 3 aya ha.

tuple = (1, 3, 3, 5, 3, 7)

count = tuple.count(3)

print(count)
--------------------------------------------------------------------
3



-------------------------------------------------------------------------------------------------------------------



# 17- Tuple - index()
# ek tuple = (10, 20, 30, 40) element 30 ka index print kro.

tuple = (10, 20, 30, 40)

index = tuple.index(30)

print(index)
------------------------------------------------------------------
2



-------------------------------------------------------------------------------------------------------------------



# 18- Tuple - sum()
# Ek tuple = (5, 10, 15, 20) sb numbers ka sum() print kro.

tuple = (5, 10, 15, 20)

print(sum(tuple))
---------------------------------------------------------------
50


-------------------------------------------------------------------------------------------------------------------


# 19- Tuple - max() and min()
# ek tuple = (22, 5, 17, 9, 33) maximum and minimum value print kro.

tuple = (22, 5, 17, 9, 33)

print(max(tuple))
print(min(tuple))
-----------------------------------------------------------------------------
33
5



-------------------------------------------------------------------------------------------------------------------




# 20- Tuple - len()
# Ek tuple = ("apple", "banana", "cherry", "mango") len() method use kr ky total iteams print kro. 

tuple = ("apple", "banana", "cherry", "mango")

print(len(tuple))
----------------------------------------------------
4
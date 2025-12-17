# 1- Write a program to creat a dictionary of urdu words with the value as their English translation. Provide user with an option to look it up!

words = {
    "Madad": "Help",
    "Kursi": "Chair",
    "Billi": "Cat",
}

word = input("Enter a word you want meaning of: ")

print(words[word])
--------------------------------------------------------------------
Enter a word you want meaning of: Kursi
Chair


-------------------------------------------------------------------------------------------------------------------


# 2- Write a program to input 8 numbers from the user and display all the unique numbers (once) set().

s = set()

n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))

print(s)
---------------------------------------------
Enter number: 5
Enter number: 1
Enter number: 2
Enter number: 5
Enter number: 3
Enter number: 1
Enter number: 2
Enter number: 3
{1, 2, 3, 5}


-------------------------------------------------------------------------------------------------------------------


# 3- Can we have a set with 18(int) and "18" (str)string as a value in it ?

s = set()
s.add(18)
s.add("18")
print(s)
------------------------------------------------
{18, '18'}


-------------------------------------------------------------------------------------------------------------------


# 4- What will be the length of following set s
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")

s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))

# is set is len() 2 is lia ayi ha q ky python integer 20 and float 20.0 ki value check karay ga or in 2no ki value same ha tou 2no ko aik---
# --- count kr ky ans 2 dia ha means int wala 20 of float wala 20.0 ko 1 count kia or str walay "20" ko elehda say count kia tou ans 2 hua.
------------------------------------------------------------
2

-------------------------------------------------------------------------------------------------------------------


# 5- s = {} what is the type of 's'?

s = {}
print(type(s))
--------------------------------------
<class 'dict'>


-------------------------------------------------------------------------------------------------------------------



# 6- Create an empty dictionary. allow 4 friends to enter their favourite language as value and use key as their names. Assume that the names are unique.

a = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
a.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
a.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
a.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
a.update({name: lang})

print(a)
----------------------------------------------
Enter friends name: Haider
Enter language name: Python
Enter friends name: Kala
Enter language name: c++
Enter friends name: Amir
Enter language name: jawa
Enter friends name: Farhan
Enter language name: jawa script
{'Haider': 'Python', 'Kala': 'c++', 'Amir': 'jawa', 'Farhan': 'jawa script'}


-------------------------------------------------------------------------------------------------------------------



# 7- If the names of 2 friends are same; What will happen to the program in Problem 6 ?

a = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
a.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
a.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
a.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
a.update({name: lang})

print(a)
-------------------------------------------------
Enter friends name: Haider
Enter language name: c
Enter friends name: Haider
Enter language name: c++
Enter friends name: Kala
Enter language name: python
Enter friends name: amir
Enter language name: python
{'Haider': 'c++', 'Kala': 'python', 'amir': 'python'}


-------------------------------------------------------------------------------------------------------------------


# 8- If the language of two friends are same; What will happen to the program in problem 6 ?

a = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
a.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
a.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
a.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
a.update({name: lang})

print(a)

# Language value ha or names key hn agr key same ho gi tou wo update ho jaya gi or ans main latest key or value aya gi lakin agr value------
# same ho gi or key different tou phr answer main koi change nahin aya ga jesay hm ny yahan code apply kr ky dakh lia.
---------------------------------------------------------
Enter friends name: Haider
Enter language name: Python
Enter friends name: Ali
Enter language name: C++
Enter friends name: Amir
Enter language name: Python
Enter friends name: Farhan
Enter language name: C
{'Haider': 'Python', 'Ali': 'C++', 'Amir': 'Python', 'Farhan': 'C'}



-------------------------------------------------------------------------------------------------------------------


# 9- Can you change the values inside the list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}
print(type(s))
# set main list nahin ho skti
# Error dy ga koi b code yahan apply karain gy tou.
----------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipython-input-3169711569.py in <cell line: 0>()
      2 # s = {8, 7, 12, "Harry", [1,2]}
      3 
----> 4 s = {8, 7, 12, "Harry", [1,2]}
      5 print(type(s))
      6 # set main list nahin ho skti

TypeError: unhashable type: 'list'


-------------------------------------------------------------------------------------------------------------------


# 10 - keys()
# Ek dictionary banao jisme 3 logon ke names aur unke marks hon.
# keys() ka use karke sirf names print karo.

marks = {
    "Haider": 75,
    "Ali": 82,
    "Hasan": 80,
}

print("Names (keys):", marks.keys())
#yeh code mujhy chapgpt ny dia ha

a = marks.keys()
print(a)
#yeh code mainay khud apply kia ha.
-----------------------------------------
Names (keys): dict_keys(['Haider', 'Ali', 'Hasan'])
dict_keys(['Haider', 'Ali', 'Hasan'])


-------------------------------------------------------------------------------------------------------------------


# 11 - values()
# Ek dictionary banao jisme 3 cities aur unke temperature hon.
# values() ka use karke sirf temperature print karo.

weather = {
    "Lahore": 35,
    "Islamabad": 28,
    "Karachi": 47,
}

print("Temperature (Values)", weather.values())

a = weather.values()
print("Temperature of different cities:", a)
-------------------------------------------------------------
Temperature (Values) dict_values([35, 28, 47])
Temperature of different cities: dict_values([35, 28, 47])


-------------------------------------------------------------------------------------------------------------------



# 12 - items()
# Ek dictionary banao jisme 3 fruits aur unke prices hon.
# items() method use karke sab key-value pairs print karo.

fruits = {
    "Mango": 150,
    "Orange": 225,
    "Apple": 100,
}

print(fruits.items())
------------------------------------------------------------
dict_items([('Mango', 150), ('Orange', 225), ('Apple', 100)])



-------------------------------------------------------------------------------------------------------------------


# 13 - update()
# Ek dictionary banao jisme ek student ka name aur marks hon.
# update() use karke uske marks change karo aur ek nayi entry bhi add karo.

marks = {
    "Haider": 81,
}

marks.update({"Haider": 90})
marks.update({"Ali": 75})
print(marks)
------------------------------------------------------
{'Haider': 90, 'Ali': 75}


-------------------------------------------------------------------------------------------------------------------



# 14 - pop()
# Ek dictionary banao jisme 3 cheezein aur unke prices hon.
# pop() method se ek item remove karo aur print karo.

a = {
    "Shirts": 1500,
    "Pants": 1950,
    "Jacket": 3800,
}

a.pop("Jacket")
print(a)
------------------------------------------------
{'Shirts': 1500, 'Pants': 1950}



-------------------------------------------------------------------------------------------------------------------


# 15 - popitem()
# Ek dictionary banao jisme 3 items hon.
# popitem() ka use karke last added item remove karo aur print karo.

footwear = {
    "Sandals": 1500,
    "Shoes": 3500,
    "Joggers": 3000,
}

footwear.popitem()
print(footwear)
-------------------------------------
{'Sandals': 1500, 'Shoes': 3500}



-------------------------------------------------------------------------------------------------------------------


# 16 - clear()
# Ek dictionary banao jisme 2 key-value pairs hon.
# clear() method ka use karke dictionary empty karo aur print karo.

food = {
    "Chicken": 1800,
    "Pasta": 1200,
}

food.clear()
print(food)
-------------------------------------
{}



-------------------------------------------------------------------------------------------------------------------




# 17 - copy()
# Ek dictionary banao aur uski copy banao.
# Dono dictionaries print karke dekho ke dono alag objects hain.

fruits = {
    "Mango": 150,
    "Orange": 225,
    "Apple": 100,
}

fruits_copy = fruits.copy()
print(fruits)
print(fruits_copy)
-----------------------------------
{'Mango': 150, 'Orange': 225, 'Apple': 100}
{'Mango': 150, 'Orange': 225, 'Apple': 100}



-------------------------------------------------------------------------------------------------------------------




# 18 - add()
# Ek empty set banao aur add() method use karke 3 numbers add karo.

a = set()
a.add(5)
a.add(7)
a.add(10)
print(a)
-----------------------------------------------------
{10, 5, 7}



-------------------------------------------------------------------------------------------------------------------




# 19 - remove()
# Ek set = {1, 2, 3, 4}
# remove() ka use karke element 3 hatao aur updated set print karo.

a = {1, 2, 3, 4}
a.remove(3)
print(a)
-----------------------------------------------------------------------
{1, 2, 4}



-------------------------------------------------------------------------------------------------------------------




# 20 - discard()
# Ek set = {10, 20, 30}
# discard() ka use karke element 50 hatao aur dekho ke koi error aata hai ya nahi.

a = {10, 20, 30}
a.discard(50)
print(a)
---------------------------------------------------
{10, 20, 30}



-------------------------------------------------------------------------------------------------------------------




# 21 - pop()
# Ek set = {"apple", "banana", "cherry"}
# pop() method use karke koi random element remove karo aur dono (element aur set) print karo.

fruits = {"apple", "banana", "cherry"}
removed_item = fruits.pop()
print(removed_item)
print(fruits)
------------------------------------------
cherry
{'banana', 'apple'}



-------------------------------------------------------------------------------------------------------------------



# 22 - clear()
# Ek set = {5, 10, 15}
# clear() method se set ko khaali karo aur print karo.

a = {5, 10, 15}
a.clear()
print(a)
-------------------------------------------
set()



-------------------------------------------------------------------------------------------------------------------







# 23 - copy()
# Ek set banao aur uski copy ek naye variable mein rakho.
# Dono sets print karo.

a = {1, 5, "Apple", 52}
b = a.copy()
print(a)
print(b)
--------------------------
{1, 'Apple', 52, 5}
{1, 'Apple', 52, 5}



-------------------------------------------------------------------------------------------------------------------


# 24 - union()
# Do sets banao, set1 = {1,2,3} aur set2 = {3,4,5}
# union() method ka use karke dono sets combine karo aur print karo.

a = {1, 2, 3}
b = {3, 4, 5}
c = a.union(b)
print(c)
------------------------------
{1, 2, 3, 4, 5}


-------------------------------------------------------------------------------------------------------------------


# 25 - intersection()
# Do sets banao, set1 = {2,4,6} aur set2 = {4,6,8}
# intersection() ka use karke common elements print karo.

a = {2,4,6}
b = {4,6,8}
result = a.intersection(b)
print(result)
--------------------------------------
{4, 6}


-------------------------------------------------------------------------------------------------------------------



# 26 - difference()
# Do sets banao, set1 = {1,2,3,4} aur set2 = {3,4,5}
# difference() ka use karke set1 ke unique elements print karo.

a = {1,2,3,4}
b = {3,4,5}
c = a.difference(b)
d = b.difference(a)
print(c)
print(d)
-------------------------------------
{1, 2}
{5}


-------------------------------------------------------------------------------------------------------------------


# 27 - symmetric_difference()
# Do sets banao, set1 = {1,2,3} aur set2 = {3,4,5}
# symmetric_difference() ka use karke un elements ko print karo jo dono mein common nahi hain.

a = {1,2,3}
b = {3,4,5}
c = a.symmetric_difference(b)
print(c)
-------------------------------------------
{1, 2, 4, 5}


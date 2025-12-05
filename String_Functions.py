String Functions

1-

# Write a program to display a user entered name followed by good afternoon using input() function.
# is function main hm ny f use kr ky string ko f string bna dia ha. 

name = input("Enter your name: ")
print(f"Good Afternoon {name}")
---------------------------------------
Enter your name: Haider
Good Afternoon Haider

-------------------------------------------------------------------------------------------------------------------

2-

# Write a program to fill in a letter template given below with name and date.

letter = '''
       Dear <|Name|>,
       You are selected!
       <|Date|>
       '''

print(letter.replace("<|Name|>", "Haider").replace("<|Date|>", "30th september 2025"))
---------------------------------------------------------------------------------------
Dear Haider,
       You are selected!
       30th september 2025

-------------------------------------------------------------------------------------------------------------------

3-

# Write a program to detect double space in a string.
# is function main agr ans -1 ho tou us ka matlab ho ga ky jo cheez ap find kr rahay ho wo us string main nahin ha.
# or agr jo cheez ap find kr rahay ho wo us string main ha tou ans main us ki index value a jaya gi.

a = "Harry is a  good boy"
print(a.find("  "))
----------------------------
10


-------------------------------------------------------------------------------------------------------------------


4-

# Replace the double space from problem 3 to single spaces.
# yahan hm ny .replace function use kr ky double space ko replace kr dia single space say.

a = "Harry is a  good boy"
print(a.replace("  ", " "))
-------------------------------
Harry is a good boy


-------------------------------------------------------------------------------------------------------------------

5-

# Write a program to format the following letter using escape sequence characters.

letter = "Dear Harry, this python course is nice. Thanks!"
print(letter)

# yahan hm \n new line or \t tab jitni space wala function or phr \n aik or new line yeh 3 escape sequence character use kia hn.
letter = "Dear Harry,\n\t This python course is nice.\n Thanks!"
print(letter)
--------------------------------------------------------------------------
Dear Harry, this python course is nice. Thanks!
Dear Harry,
	 This python course is nice.
 Thanks!

-------------------------------------------------------------------------------------------------------------------
                          

6-

#User se ek sentence input lo aur uski length print karo.

sentence = input("Enter a sentence: ")
print("Length of a sentence is: ", len(sentence))
---------------------------------------------------
Enter a sentence: My name is Haider
Length of a sentence is:  17

-------------------------------------------------------------------------------------------------------------------

7-

#user say aik word input lo aur check kro ke sentence us word se start hota ha ya nahin.

sentence = input("Enter a sentence: ")
word = input("Enter a word to check start: ")
print("Does the sentence start with yout word? ->", sentence.startswith(word))
-------------------------------------------------------------------------------
Enter a sentence: My name is haider
Enter a word to check start: My
Does the sentence start with yout word? -> True


-------------------------------------------------------------------------------------------------------------------


8-

#sentence ky frist 5 characters and last 5 characters print karo.
word = "Defaulter"
print("First 5 characters: ", word[:5])
print("Last 5 characters: ", word[-5:])
-----------------------------------------
First 5 characters:  Defau
Last 5 characters:  ulter

-------------------------------------------------------------------------------------------------------------------


9-

#User ka name input lo aur usko uppercase and lowercase me print karo.
name = input("Enter your name: ")
print(name.upper())
print(name.lower())
------------------------------------
Enter your name: Haider
HAIDER
haider

-------------------------------------------------------------------------------------------------------------------

10-

#user say aik word input lo aur sentence me us word ko "Python" se replace karo.

sentence = "I love programming"
replace_word = input("Enter a word to raplace: ")
new_sentence = sentence.replace(replace_word, "Pyton")

print(new_sentence)
--------------------------------------------------------
Enter a word to raplace: programming
I love Pyton


-------------------------------------------------------------------------------------------------------------------


11-

#Aik word input lo aur check karo ke wo palindrome hai ya nahin.(palindrome ulta seedha same word jesay madam)

word = input("Enter a word to check palindrome: ")
if word == word[ : : -1] :
   print("Yes it is a palindrome")
else:
   print("No it is not a palindrome")
---------------------------------------------------------
Enter a word to check palindrome: madam
Yes it is a palindrome


-------------------------------------------------------------------------------------------------------------------

12-

#Check kro sentence dia huya word say end hta ha ya nahin

line = "Python is great"
print(line.endswith("great"))
-------------------------------
True


-------------------------------------------------------------------------------------------------------------------

13-

#Remove extra spaces at start/End.

word = "  Hello World   "
print(word.strip())
----------------------------
Hello World


-------------------------------------------------------------------------------------------------------------------


14-

#Count how many times a word appears.

letter = "Hello this is haider and haider is 33 years of age."
print(letter.count("haider"))
------------------------------------------------------------
2

-------------------------------------------------------------------------------------------------------------------


15-

#user say aik sentence input lo aur uska sirf pehla letter capital banao.

name = input("Enter your name: ")
print(name.capitalize())
-------------------------------------
Enter your name: my name is haider
My name is haider


-------------------------------------------------------------------------------------------------------------------

16-

# user say aik sentence input lo aur us kay har word ka pehla letter capital banao

hello = input("Enter your sentence: ")
print(hello.title())
------------------------------------------
Enter your sentence: my name is haider.
My Name Is Haider.


-------------------------------------------------------------------------------------------------------------------

17-

# user say aik sentence input lo aur usme har capital letter ko small or har small letter ko capital banao.

hi = input("Enter your sentence: ")
print(hi.swapcase())
--------------------------------------
Enter your sentence: My Name Is Haider
mY nAME iS hAIDER
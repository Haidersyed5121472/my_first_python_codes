# Practice exercises for File I/O in Python.

# File Reader

f = open("notes.txt", "r")
file = f.read()
print(file)

f.close()


# File Write Mode

f = open("student.txt" , "w")
student = f.write("i love python")
print(student)

f.close()


# File Append Mode

f = open("student.txt" , "a")
addition = f.write("\nI am improving my python skills.")
print(addition)

f.close()


# Activity Logger (File Append Practice)

activity = input("Enter your activity: ")
f = open("log.txt", "a")
new_activity = f.write("\n" + activity)
print(new_activity)

print("Activity saved successfully")

f.close()


# Read First Line From File

f = open("log.txt", "r")
file = f.readline()
print(file)

f.close()


# Read All Lines Using Loop

f = open("log.txt", "r")
file_1 = f.readlines()
for i in file_1:
    print(i)


f.close()


# Count Total Lines In File (Using Loop)

f = open("log.txt", "r")
file = f.readlines()
total = 0
for i in file:
    total += 1
print(total)


f.close()


# Count Total Lines In File (Using len)

f = open("log.txt", "r")
file = f.readlines()
print(len(file))


f.close()


# Search Fixed Word In File

f = open("log.txt", "r")
file = f.read().lower()
if "python" in file:
    print("word found")
else:
    print("word not found")


f.close()


# Search User Input Word In File

f = open("log.txt", "r")
file = f.read().lower()
word = input("Enter a word: ").lower()
if word in file:
    print("word found")
else:
    print("word not found")


f.close()
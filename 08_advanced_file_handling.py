# Create and Write to a File

f = open("01_notes.txt", "w")
file = f.write("Learning python file handling.")


print("File Created")

f.close()


# Read Data from File

f = open("notes.txt", "r")
file = f.read()
print(file)

f.close()


# Append New Data to File

f = open("01_notes.txt", "a")
z = f.write("\nLearning advanced file handling.")
print(z)

f.close()


# Read File Line by Line

f = open("notes.txt", "r")
file = f.readline()
file_1 = f.readline()
print(file)
print(file_1)

f.close()


# Count a Specific Word in File

f = open("notes.txt", "r")
word = input("Enter the word: ").lower()
file = f.read().lower()
z = file.count(word)
print(z)

f.close()


# Count Total Words in File

f = open("notes.txt", "r")
file = f.read().split()
z = len(file)
print(z)

f.close()


# Replace a Specific Word in File

f = open("notes.txt", "r") 
file = f.read() 
z = file.replace("programming", "python")

file_a = open("notes.txt", "w")
file_a.write(z)

f.close()
file_a.close()


# Copy Content from One File to Another

f = open("notes.txt", "r")
file = f.read()

a = open("backup.txt", "w")
a.write(file)

f.close()
a.close()

y = open("backup.txt", "r")
y_file = y.read()
print(y_file)

y.close()


# Read File Using With Open

with open("notes.txt", "r") as f:
    file = f.read()
    print(file)


# Write Data to File Using With Open

with open("practice.txt", "w") as f:
    writing = f.write("Python automation is fun.")
    print(writing)


# Append Data to File Using With Open

with open("practice.txt", "a") as f:
    writing = f.write("\nI am learning file automation.")
    print(writing)


# Read File Line by Line Using With Open

with open("practice.txt", "r") as f:
    for i in f:
        print(i)


# Count Total Lines in File Using Loop and With Open

with open("practice.txt", "r") as f:
    count = 0
    for i in f:
        count += 1
    print(count)


# Search User Input Word in File Using With Open

with open("practice.txt", "r") as f:
    file = f.read().lower()
    word = input("Enter a word you want to find: ").lower()
    if word in file:
        print("Word found")
    else:
        print("Word not found")


# Check File Exists Before Reading Using With Open Style Logic
# Check if file exists or not before opening
# If file exists then read and print content
# If file does not exist then print "File not found"

import os
file = input("Enter a file name: ")
file_exist = os.path.exists(file)
if file_exist:
        with open(file, "r") as f:
              reading_file = f.read()
              print(reading_file)
else:
    print("File not found")


# Write Multiple Lines to File Using Writelines and With Open

# Create a file named report.txt
# Write multiple lines to file
# Use writelines()
# Use with open()



with open("report.txt", "w") as f:
    line_1 = "I am learning file handling in python."
    line_2 = "\nI love it."
    file_1 = (line_1 , line_2)
    file = f.writelines(file_1)
    print(file)


# Extract Only Matching Lines From File

# Read file using with open()
# Print only lines containing "python"
# Ignore uppercase/lowercase issue
# Use loop
# Do not use read() or readlines()


with open("practice.txt", "r") as f:
    for i in f:
        if "python".lower() in i.lower():
            print(i)


# Count Matching Lines in File

# Read file using with open()
# Count how many lines contain "python"
# Ignore uppercase/lowercase issue
# Use loop
# Do not use read() or readlines()


with open("practice.txt", "r") as f:
    total = 0
    for i in f:
        if "python".lower() in i.lower():
            total += 1
    print(total)


# Save Matching Lines to New File

# Read practice.txt using with open()
# Find lines containing "python"
# Ignore uppercase/lowercase issue
# Save matching lines into a new file named filtered.txt
# Use loop
# Do not use read() or readlines()


with open("practice.txt", "r") as f:
        with open("filtered.txt", "w") as z:
              for i in f:
                  if "python".lower() in i.lower():
                       z.write(i)


# Remove Empty Lines From File

# Read practice.txt using with open()
# Ignore empty lines
# Save non-empty lines into cleaned.txt
# Use loop
# Do not use read() or readlines()


with open("practice.txt", "r") as f:
        with open("cleaned.txt", "w") as z:
              for i in f:
                  if len(i.strip()) >=1:
                        z.write(i)



# Create Backup File Before Editing

# Check if practice.txt exists
# Create extrabackup.txt
# Copy all content from practice.txt to backup.txt
# Use with open()
# Use loop
# Do not use read() or readlines()

import os

file_exists = os.path.exists("practice.txt")
if file_exists:
    with open ("practice.txt", "r") as f:
        with open ("extrabackup.txt", "w") as z:
            for i in f:
                z.write(i)

else:
    print("File does not exist")
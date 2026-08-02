import pathlib

# Practice Question # 7
#
# Import the built-in "pathlib" module.
#
# Create a folder named:
#
# Journal
#
# Inside the "Journal" folder,
# create a file named:
#
# daily_log.txt
#
# Then:
#
# 1. Write the following text into the file:
#
# Day 1: Learned Path.open()
#
# 2. Open the same file in append mode
#    and add:
#
# Day 2: Practiced append mode
#
# 3. Read the complete file content.
#
# 4. Print the file content.
#
# 5. Print whether the file exists.
#
# 6. Print the absolute path of the file.
#
# Methods / Properties to Practice:
#
# Path()
# mkdir()
# touch()
# open()
# exists()
# resolve()


import shutil

shutil.rmtree("Journal")
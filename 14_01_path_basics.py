import pathlib

# Practice Question # 1
#
# Import the built-in "pathlib" module.
#
# Create a Path object that represents your current
# working directory.
#
# Then:
#
# 1. Print the Path object.
# 2. Print its data type.
# 3. Print only the folder name (last part of the path).
# 4. Print all parts of the path as a tuple.
#
# Methods / Properties to Practice:
#
# Path()
# Path.cwd()
# name
# parts

path = pathlib.Path.cwd()

print(path)
print(type(path))
print(path.name)
print(path.parts)



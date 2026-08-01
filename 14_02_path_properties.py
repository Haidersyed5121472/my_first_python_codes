import pathlib

# Practice Question # 2
#
# Import the built-in "pathlib" module.
#
# Create a Path object that represents a file named:
#
# "reports/sales_report.pdf"
#
# (Do not create the actual file.)
#
# Then print:
#
# 1. The complete Path object.
# 2. The parent folder.
# 3. The file name.
# 4. The file name without extension.
# 5. The file extension.
# 6. Your home directory.
#
# Methods / Properties to Practice:
#
# Path()
# Path.home()
# parent
# name
# stem
# suffix

file = "reports/sales_report.pdf"
path = pathlib.Path(file)
file_1 = pathlib.Path.home()
print(path)
print(file_1)
print(path.parent)
print(path.name)
print(path.stem)
print(path.suffix)



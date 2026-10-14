# Practice Question #4

# Import the required library.
# Open the existing "products.xlsx" workbook.
# Select the active worksheet.
# Read the value from cell A1 and print it.
# Read the value from cell A2 and print it.
# Read the value from cell B2 and print it.

from openpyxl import load_workbook


workbook = load_workbook("products.xlsx") # Open the existing "products.xlsx" workbook.
sheet = workbook.active # Select the active worksheet.
print(sheet["A1"].value) # Read the value from cell A1 and print it.
print(sheet["A2"].value) # Read the value from cell A2 and print it.
print(sheet["B2"].value) # Read the value from cell B2 and print it.



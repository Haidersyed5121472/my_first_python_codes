# Practice Question #9

# Import the required library.
# Open the existing "products.xlsx" workbook.
# Select the active worksheet.
# Read all values from row 2.
# Print each value in row 2.


from openpyxl import load_workbook

wb = load_workbook("products.xlsx") # Open the existing "products.xlsx" workbook.
sheet = wb.active # Select the active worksheet.

for row in sheet[2]: # Use for loop to read all values from row 2.
    print(row.value) # Print each value in row 2.



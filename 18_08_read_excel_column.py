# Practice Question #8

# Import the required library.
# Open the existing "products.xlsx" workbook.
# Select the active worksheet.
# Read all values from column A.
# Print each value in column A.


from openpyxl import load_workbook

wb = load_workbook("products.xlsx") # Open the existing "products.xlsx" workbook.
sheet = wb.active # Select the active worksheet.

for column in sheet["A"]: # Use a for loop to go through all cells in column A.
    print(column.value) # Print the values of column A




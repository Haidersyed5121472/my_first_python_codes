# Practice Question #7

# Import the required library.
# Open the existing "products.xlsx" workbook.
# Select the active worksheet.
# Use a loop to go through all rows in the worksheet.
# Print the values of each row.


from openpyxl import load_workbook

wb = load_workbook("products.xlsx") # Open the existing "products.xlsx" workbook.
sheet = wb.active # Select the active worksheet.

for row in sheet: # Use a loop to go through all rows in the worksheet.
    for cell in row: # Loop through each cell in the current row.
        print(cell.value) # Print the values of each row.



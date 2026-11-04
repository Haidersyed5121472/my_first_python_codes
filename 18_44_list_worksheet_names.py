# Practice Question #44

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Get the names of all worksheets in the workbook.
# Print the worksheet names.

from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
sheet_names = wb.sheetnames # Get the names of all worksheets in the workbook.

print(sheet_names) # Print the worksheet names.




# Practice Question #35

# Import the required library.
# Open the existing "products.xlsx" workbook.
# Select the active worksheet.
# Set the width of column A to 25.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook

wb = load_workbook("products.xlsx") # Open the existing "products.xlsx" workbook.
ws = wb.active # Select the active worksheet.

ws.column_dimensions["A"].width = 25 # Set the width of column A to 25.

wb.save("products.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.



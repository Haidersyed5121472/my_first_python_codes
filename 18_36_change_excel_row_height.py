
# Practice Question #36

# Import the required library.
# Open the existing "products.xlsx" workbook.
# Select the active worksheet.
# Set the height of row 1 to 30.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook

wb = load_workbook("products.xlsx") # Open the existing "products.xlsx" workbook.
ws = wb.active # Select the active worksheet.

ws.row_dimensions[1].height = 30 # Set the height of row 1 to 30.

wb.save("products.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.



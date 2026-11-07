# Practice Question #49

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "Sales".
# Delete one row at row 2.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["Sales"] # Select the worksheet named "Sales".

ws.delete_rows(2) # Delete one row at row 2.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.





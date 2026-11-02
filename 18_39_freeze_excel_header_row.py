# Practice Question #39

# Import the required library.
# Open the existing "products.xlsx" workbook.
# Select the active worksheet.
# Freeze the top row.
# Save the updated workbook.
# Print a success message.


from openpyxl import load_workbook

wb = load_workbook("products.xlsx") # Open the existing "products.xlsx" workbook.
ws = wb.active # Select the active worksheet.

ws.freeze_panes = "A2" # Freeze the top row.

wb.save("products.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




# Practice Question #37

# Import the required library.
# Open the existing "products.xlsx" workbook.
# Select the active worksheet.
# Merge cells A5 and B5.
# Save the updated workbook.
# Print a success message.


from openpyxl import load_workbook


wb = load_workbook("products.xlsx") # Open the existing "products.xlsx" workbook.
ws = wb.active # Select the active worksheet.

ws.merge_cells("A5:B5") # Merge cells A5 and B5.

wb.save("products.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.





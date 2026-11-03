# Practice Question #41

# Import the required library.
# Open the existing "products.xlsx" workbook.
# Select the active worksheet.
# Set the print area from cell A1 to C4.
# Save the updated workbook.
# Print a success message.


from openpyxl import load_workbook

wb = load_workbook("products.xlsx") # Open the existing "products.xlsx" workbook.
ws = wb.active # Select the active worksheet.

ws.print_area = "A1:C4" # Set the print area from cell A1 to C4.

wb.save("products.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.





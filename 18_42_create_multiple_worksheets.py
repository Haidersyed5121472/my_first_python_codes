# Practice Question #42

# Import the required library.
# Create a new Excel workbook.
# Rename the active worksheet to "G_Products".
# Create a new worksheet named "Sales".
# Create another worksheet named "Customers".
# Save the workbook as "shop_data.xlsx".
# Print a success message.


import openpyxl

wb = openpyxl.Workbook() # Create a new Excel workbook.
ws = wb.active # Select the active worksheet.

ws.title = "G_Products" # Rename the active worksheet to "G_Products".

sheet_1 = wb.create_sheet("Sales") # Create a new worksheet named "Sales".
sheet_2 = wb.create_sheet("Customers") # Create another worksheet named "Customers".

wb.save("shop_data.xlsx") # Save the workbook as "shop_data.xlsx".
print("New workbook and multiple worksheets created successfully.") # Print a success message.





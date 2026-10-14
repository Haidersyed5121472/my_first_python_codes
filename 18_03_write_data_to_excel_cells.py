# Practice Question #3

# Import the required library.
# Create a new Excel workbook.
# Select the active worksheet.
# Write "Product" into cell A1.
# Write "Price" into cell B1.
# Write "Baby Suit" into cell A2.
# Write 525 into cell B2.
# Save the workbook as "products.xlsx".

import openpyxl

wb = openpyxl.Workbook() # Create a new Excel workbook.
work_sheet = wb.active # Select the active worksheet.
work_sheet.title = "Products" # Rename the active worksheet to "Products".

work_sheet["A1"] = "Product" # Write "Product" into cell A1.
work_sheet["B1"] = "Price" # Write "Price" into cell B1.

work_sheet["A2"] = "Baby Suit" # Write "Baby Suit" into cell A2.
work_sheet["B2"] = 525 # Write 525 into cell B2.

wb.save("products.xlsx") # Save the workbook as "products.xlsx".


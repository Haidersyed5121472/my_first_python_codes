# Practice Question #11

# Import the required library.
# Create a new Excel workbook.
# Select the active worksheet.
# Rename the worksheet to "Products".
# Add the following headers:
# Product, Price
# Add three products with their prices:
# Baby Suit, 600
# Baby Shoes, 350
# Baby Cap, 150
# Save the workbook as "products_multiple.xlsx".
# Print a success message.

import openpyxl

create_workbook = openpyxl.Workbook() # Create a new Excel workbook.
work_sheet = create_workbook.active # Select the active worksheet.

work_sheet.title = "Products" # Rename the worksheet to "Products".

sheet = [
    ["Product", "Price"],
    ["Baby Suit", 600],
    ["Baby Shoes", 350],
    ["Baby Cap", 150]
    ] # Create the list of lists and store it in a variable.
for row in sheet: # Use for loop to go through the sheet.
    work_sheet.append(row) # Use .append() to add each row to the worksheet.

create_workbook.save("products_multiple.xlsx") # Save the workbook as "products_multiple.xlsx".
print("Updated workbook created successfully") # Print a success message.



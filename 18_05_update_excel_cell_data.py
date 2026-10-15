# Practice Question #5

# Import the required library.
# Open the existing "products.xlsx" workbook.
# Select the active worksheet.
# Change the price of "Baby Suit" in cell B2 from 525 to 600.
# Add "Baby Shoes" into cell A3.
# Add 350 into cell B3.
# Save the changes to "products.xlsx".
# Print a message confirming that the workbook was updated.

from openpyxl import load_workbook

workbook = load_workbook("products.xlsx") # Open the existing "products.xlsx" workbook.
sheet = workbook.active # Select the active worksheet.

sheet["B2"] = 600 # Change the price of "Baby Suit" in cell B2 from 525 to 600.
sheet["A3"] = "Baby Shoes" # Add "Baby Shoes" into cell A3.
sheet["B3"] = 350 # Add 350 into cell B3.

workbook.save("products.xlsx") # Save the changes to "products.xlsx".
print("Workbook updated successfully.") # Print a message confirming that the workbook was updated.




# Practice Question #63

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "G_Products".
# Select cell C2.
# Apply date number format "DD-MM-YYYY" to cell C2.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["G_Products"] # Select the worksheet named "G_Products".

cell = ws["C2"] # Select cell C2.
cell.number_format = "DD-MM-YYYY" # Apply date number format "DD-MM-YYYY" to cell C2.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




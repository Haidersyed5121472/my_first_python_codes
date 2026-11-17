# Practice Question #66

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "G_Products".
# Select cell B2.
# Apply number format with comma separators and no decimal places.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["G_Products"] # Select the worksheet named "G_Products".

cell = ws["B2"] # Select cell B2.
cell.number_format = "#,##0" # Apply number format with comma separators and no decimal places.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




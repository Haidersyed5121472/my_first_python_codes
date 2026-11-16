# Practice Question #64

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "G_Products".
# Select cell B4.
# Apply decimal number format with two decimal places to cell B4.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["G_Products"] # Select the worksheet named "G_Products".

cell = ws["B4"] # Select cell B4.
cell.number_format = "0.00" # Apply decimal number format with two decimal places to cell B4.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




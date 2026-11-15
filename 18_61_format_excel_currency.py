# Practice Question #61

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "G_Products".
# Select cell B2.
# Apply Pakistani Rupees (PKR) currency number format to cell B2.
# Save the updated workbook.
# Print a success message.


from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["G_Products"] # Select the worksheet named "G_Products".

cell = ws["B2"] # Select cell B2.
cell.number_format = "Rs #,##0.00" # Apply Pakistani Rupees (PKR) currency number format to cell B2.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.


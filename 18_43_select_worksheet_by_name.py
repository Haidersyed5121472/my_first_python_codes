# Practice Question #43

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "Sales".
# Write "Product" in cell A1.
# Write "Quantity" in cell B1.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx" ) # Open the existing "shop_data.xlsx" workbook.
ws = wb["Sales"] # Select the worksheet named "Sales".

ws["A1"] = "Product" # Write "Product" in cell A1.
ws["B1"] = "Quantity" # Write "Quantity" in cell B1.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




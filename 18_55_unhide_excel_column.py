# Practice Question #55

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "Sales".
# Unhide column B.
# Save the updated workbook.
# Print a success message.


from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["Sales"] # Select the worksheet named "Sales".

ws.column_dimensions["B"].hidden = False # Unhide column B.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




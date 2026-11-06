# Practice Question #47

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "Sales".
# Create a copy of the selected worksheet.
# Rename the copied worksheet to "Sales_Copy".
# Save the updated workbook.
# Print a success message.


from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["Sales"] # Select the worksheet named "Sales".

copied_ws = wb.copy_worksheet(ws) # Create a copy of the selected worksheet.
copied_ws.title = "Sales_Copy" # Rename the copied worksheet to "Sales_Copy".

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.





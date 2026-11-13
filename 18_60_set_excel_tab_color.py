# Practice Question #60

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "Sales_Copy".
# Set the worksheet tab color to orange.
# Save the updated workbook.
# Print a success message.


from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["Sales_Copy"] # Select the worksheet named "Sales_Copy".

ws.sheet_properties.tabColor = "FFA500" # Set the worksheet tab color to orange.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




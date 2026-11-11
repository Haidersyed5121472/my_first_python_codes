# Practice Question #56

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "Sales".
# Set the worksheet tab color to red.
# Save the updated workbook.
# Print a success message.


from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["Sales"] # Select the worksheet named "Sales".

ws.sheet_properties.tabColor = "FF0000" # Set the worksheet tab color to red.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




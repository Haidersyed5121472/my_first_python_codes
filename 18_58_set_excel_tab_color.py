# Practice Question #58

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "G_Products".
# Set the worksheet tab color to blue.
# Save the updated workbook.
# Print a success message.


from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["G_Products"] # Select the worksheet named "G_Products".

ws.sheet_properties.tabColor = "0000FF" # Set the worksheet tab color to blue.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




# Practice Question #45

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "Customers".
# Rename the worksheet to "Clients".
# Save the updated workbook.
# Print a success message.


from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["Customers"] # Select the worksheet named "Customers".

ws.title = "Clients" # Rename the worksheet to "Clients".
wb.save("shop_data.xlsx") # Save the updated workbook.

print("Workbook renamed and saved successfully.") # Print a success message.



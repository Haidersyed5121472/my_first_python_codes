# Practice Question #46

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "Clients".
# Delete the selected worksheet from the workbook.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["Clients"] # Select the worksheet named "Clients".

del wb["Clients"] # Delete the selected worksheet from the workbook.
wb.save("shop_data.xlsx") # Save the updated workbook.

print("Worksheet deleted and updated workbook saved successfully.") # Print a success message.




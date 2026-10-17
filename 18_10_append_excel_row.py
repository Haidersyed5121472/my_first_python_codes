# Practice Question #10

# Import the required library.
# Open the existing "products.xlsx" workbook.
# Select the active worksheet.
# Add a new row with the following data:
# Product: Baby Cap
# Price: 150
# Save the updated workbook.
# Print a success message.


from openpyxl import load_workbook

wb = load_workbook("products.xlsx") # Open the existing "products.xlsx" workbook.
sheet = wb.active # Select the active worksheet.

sheet.append(["Baby Cap", 150]) # Add a new row using .append() method.
wb.save("products.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.



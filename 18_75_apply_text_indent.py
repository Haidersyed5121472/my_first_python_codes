# Practice Question #75

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "G_Products".
# Select cell A1.
# Set the text indentation to 2 for cell A1.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook
from openpyxl.styles import Alignment

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["G_Products"] # Select the worksheet named "G_Products".

cell = ws["A1"] # Select cell A1.
cell.alignment = Alignment(indent=2) # Set the text indentation to 2 for cell A1.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.





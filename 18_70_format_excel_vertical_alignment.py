# Practice Question #70

# Import the required library.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "G_Products".
# Select cell A1.
# Set the vertical alignment of the cell to center.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook
from openpyxl.styles import Alignment

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["G_Products"] # Select the worksheet named "G_Products".

cell = ws["A1"] # Select cell A1.
cell.alignment = Alignment(vertical="center") # Set the vertical alignment of the cell to center.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




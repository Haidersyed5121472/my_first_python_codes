# Practice Question #79

# Import the required libraries.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "G_Products".
# Apply conditional formatting to cells B2:B10.
# Highlight cells with values between 300 and 500.
# Use a light blue fill color for matching cells.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from openpyxl.formatting.rule import CellIsRule

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["G_Products"] # Select the worksheet named "G_Products".

blue_fill = PatternFill(
    start_color="DDEBF7",
    end_color="DDEBF7",
    fill_type="solid"
) # Use a light blue fill color for matching cells.

rule = CellIsRule(
    operator="between",
    formula=["300", "500"],
    fill=blue_fill
) # Highlight cells with values between 300 and 500.

ws.conditional_formatting.add("B2:B10", rule) # Apply conditional formatting to cells B2:B10.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




# Practice Question #80

# Import the required libraries.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "G_Products".
# Apply conditional formatting to cells B2:B10.
# Highlight cells with values not equal to 500.
# Use a light orange fill color for matching cells.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from openpyxl.formatting.rule import CellIsRule

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["G_Products"] # Select the worksheet named "G_Products".

orange_fill = PatternFill(
    start_color="FCE4D6",
    end_color="FCE4D6",
    fill_type="solid"
) # Use a light orange fill color for matching cells.

rule = CellIsRule(
    operator="notEqual",
    formula=["500"],
    fill=orange_fill
) # Highlight cells with values not equal to 500.

ws.conditional_formatting.add("B2:B10", rule) # Apply conditional formatting to cells B2:B10.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




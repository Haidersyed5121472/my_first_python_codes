# Practice Question #83

# Import the required libraries.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "G_Products".
# Apply conditional formatting to cells B2:B10.
# Highlight duplicate values in the selected range.
# Use a light red fill color for duplicate values.
# Save the updated workbook.
# Print a success message.

from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from openpyxl.formatting.rule import DuplicateRule

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["G_Products"] # Select the worksheet named "G_Products".

red_fill = PatternFill(
    start_color="FFC7CE",
    end_color="FFC7CE",
    fill_type="solid"
) # Use a light red fill color for duplicate values.
rule = DuplicateRule(
    fill=red_fill
) # Highlight duplicate values in the selected range.
ws.conditional_formatting.add("B2:B10", rule) # Apply conditional formatting to cells B2:B10.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.




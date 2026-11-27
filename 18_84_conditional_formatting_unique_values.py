# Practice Question #84

# Import the required libraries.
# Open the existing "shop_data.xlsx" workbook.
# Select the worksheet named "G_Products".
# Apply conditional formatting to cells B2:B10.
# Highlight unique values in the selected range.
# Use a light green fill color for unique values.
# Save the updated workbook.
# Print a success message.


from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from openpyxl.formatting.rule import UniqueRule

wb = load_workbook("shop_data.xlsx") # Open the existing "shop_data.xlsx" workbook.
ws = wb["G_Products"] # Select the worksheet named "G_Products".

green_fill = PatternFill(
    start_color="C6EFCE",
    end_color="C6EFCE",
    fill_type="solid"
) # Use a light green fill color for unique values.
rule = UniqueRule(
    fill=green_fill
) # Highlight unique values in the selected range.
ws.conditional_formatting.add("B2:B10", rule) # Apply conditional formatting to cells B2:B10.

wb.save("shop_data.xlsx") # Save the updated workbook.
print("Updated workbook saved successfully.") # Print a success message.





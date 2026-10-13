# Practice Question #2

# Import the required library.
# Create a new Excel workbook.
# Save the workbook with the filename "students.xlsx".
# Print a message confirming that the workbook was saved.

import openpyxl

create_workbook = openpyxl.Workbook() # Create a new Excel workbook.
sheet = create_workbook.active # Store workbook in a variable.
sheet.title = "students" # Create the title.
create_workbook.save("students.xlsx") # Save the workbook with the filename "students.xlsx".
print("workbook was saved") # Print the success message.



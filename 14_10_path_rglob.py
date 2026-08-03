import pathlib

# Practice Question # 10
#
# Import the built-in "pathlib" module.
#
# Create the following folder structure:
#
# Company
# ├── report.pdf
# ├── notes.txt
# ├── HR
# │   ├── employees.csv
# │   └── salaries.xlsx
# └── Finance
#     ├── budget.xlsx
#     ├── invoice.pdf
#     └── Accounts
#         └── transactions.csv
#
# Requirements:
#
# 1. Create all folders.
# 2. Create all files.
#
# Then:
#
# 1. Use rglob("*.pdf") to print all PDF files.
# 2. Use rglob("*.csv") to print all CSV files.
# 3. Use rglob("*.xlsx") to print all Excel files.
#
# Print only the file names.
#
# Expected Output (similar to):
#
# PDF Files:
# report.pdf
# invoice.pdf
#
# CSV Files:
# employees.csv
# transactions.csv
#
# Excel Files:
# salaries.xlsx
# budget.xlsx
#
# Methods / Properties to Practice:
#
# Path()
# mkdir()
# touch()
# rglob()
# name


import pathlib

company_folder = pathlib.Path("Company") # Path for folder

report_file = pathlib.Path("Company/report.pdf") # Path for file
notes_file = pathlib.Path("Company/notes.txt") # Path for file

hr_folder = pathlib.Path("Company/HR") # Path for subfolder
employee_file = pathlib.Path("Company/HR/employees.csv") # Path for file
salaries_file = pathlib.Path("Company/HR/salaries.xlsx") # Path for file

finance_folder = pathlib.Path("Company/Finance") # Path for subfolder
budget_file = pathlib.Path("Company/Finance/budget.xlsx") # Path for file
invoice_file = pathlib.Path("Company/Finance/invoice.pdf") # Path for file

accounts_folder = pathlib.Path("Company/Finance/Accounts") # Path for subfolder
transactions_file = pathlib.Path("Company/Finance/Accounts/transactions.csv") # Path for file

company_folder.mkdir(exist_ok=True) # Create the folder using the Path object

report_file.touch(exist_ok=True) # Create the file using the Path object
notes_file.touch(exist_ok=True) # Create the file using the Path object

hr_folder.mkdir(exist_ok=True) # Create the subfolder using the Path object
employee_file.touch(exist_ok=True) # Create the file using the Path object
salaries_file.touch(exist_ok=True) # Create the file using the Path object

finance_folder.mkdir(exist_ok=True) # Create the subfolder using the Path object
budget_file.touch(exist_ok=True) # Create the file using the Path object
invoice_file.touch(exist_ok=True) # Create the file using the Path object

accounts_folder.mkdir(exist_ok=True) # Create the subfolder using the Path object
transactions_file.touch(exist_ok=True) # Create the file using the Path object

for item in company_folder.rglob("*.pdf"): # Use a for loop with the rglob() method
    print("PDF Files",item.name) # Print the matching file name

for item in company_folder.rglob("*.csv"): # Use a for loop with the rglob() method
    print("CSV Files",item.name) # Print the matching file name

for item in company_folder.rglob("*.xlsx"): # Use a for loop with the rglob() method
    print("XLSX Files",item.name) # Print the matching file name

# wrote a code in another way 


import pathlib

company_folder = pathlib.Path("Company")

report_file = pathlib.Path(company_folder,"report.pdf")
notes_file = pathlib.Path(company_folder,"notes.txt")

hr_folder = pathlib.Path(company_folder,"HR")
employee_file = pathlib.Path(hr_folder,"employees.csv")
salaries_file = pathlib.Path(hr_folder,"salaries.xlsx")

finance_folder = pathlib.Path(company_folder,"Finance")
budget_file = pathlib.Path(finance_folder,"budget.xlsx")
invoice_file = pathlib.Path(finance_folder,"invoice.pdf")

accounts_folder = pathlib.Path(finance_folder,"Accounts")
transactions_file = pathlib.Path(accounts_folder,"transactions.csv")

company_folder.mkdir(exist_ok=True)

report_file.touch(exist_ok=True)
notes_file.touch(exist_ok=True)

hr_folder.mkdir(exist_ok=True)
employee_file.touch(exist_ok=True)
salaries_file.touch(exist_ok=True)

finance_folder.mkdir(exist_ok=True)
budget_file.touch(exist_ok=True)
invoice_file.touch(exist_ok=True)

accounts_folder.mkdir(exist_ok=True)
transactions_file.touch(exist_ok=True)

for item in company_folder.rglob("*.pdf"):
    print("PDF Files",item.name)

for item in company_folder.rglob("*.csv"):
    print("CSV Files",item.name)

for item in company_folder.rglob("*.xlsx"):
    print("XLSX Files",item.name)


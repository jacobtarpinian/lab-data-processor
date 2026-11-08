import pandas as pd
from pathlib import Path


def load_data(file_path, sheet_name=0, header_row=0):

    file_path = Path(file_path.strip().strip('"'))

    # Check if file exists
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Check file extension
    if file_path.suffix.lower() != ".xlsx":
        raise ValueError("Please provide an Excel (.xlsx) file.")

    #Check sheet exists
    sheets = pd.ExcelFile(file_path).sheet_names #array of names
    
    #Check row input is valid
    if header_row<0:
        raise ValueError("Please input a valid header row. ")

    if isinstance(sheet_name, int):
        if sheet_name<0 or sheet_name >= len(sheets):
            raise ValueError("Sheet does not exist. ")
   
    else:
        if not (sheet_name in sheets):
            raise ValueError(f"Sheet not found. \nAvailable sheets: {sheets}")


    # Read Excel worksheet
    data = pd.read_excel(file_path, sheet_name=sheet_name, header=header_row)


    return data

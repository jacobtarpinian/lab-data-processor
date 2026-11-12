import pandas as pd

from validation import check_path, check_sheet, check_header


def load_data(file_path, sheet_number=0, header_row=0):

    file_path = check_path(file_path)
    check_sheet(file_path, sheet_number)
    check_header(header_row)

    data = pd.read_excel(file_path, sheet_name=sheet_number, header=header_row)
    data.columns = data.columns.str.strip()
    return data

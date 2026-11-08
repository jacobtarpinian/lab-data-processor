from data_loader import load_data
from validation import ask_file_path, ask_sheet, ask_header

file_path = ask_file_path()
sheet_number = ask_sheet(file_path)
header_row = ask_header()

data = load_data(file_path, sheet_number, header_row)

print("\nImported data:")
print(data)

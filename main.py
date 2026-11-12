from data_loader import load_data
from validation import ask_file_path, ask_sheet, ask_header
from plotter import plot_data
from formula import ask_formula

file_path = ask_file_path()
sheet_number = ask_sheet(file_path)
header_row = ask_header()

data = load_data(file_path, sheet_number, header_row)

print("\nImported data:")
print(data)

print("Available columns:", list(data.columns))

x_label, x_data = ask_formula(data, "Enter the x-axis (abscissa) expression: ")
y_label, y_data = ask_formula(data, "Enter the y-axis (ordinate) expression: ")

plot_data(x_data, y_data, x_label, y_label, f"{y_label} vs {x_label}")

from data_loader import load_data
from plotter import plot_data

while True:

    file_path = input("Enter the Excel file path: ")

    try:
    
        sheet_number = int(input("Enter sheet number: ")) - 1
        
        header_row = int(input("Input header row #: ")) -1

        data = load_data(file_path, sheet_number, header_row)
        print("\nFile loaded successfully!")
        break

    except FileNotFoundError:
        print("File not found. Please try again.\n")

    except ValueError as error:
        print(f"{error}\n")

    except PermissionError:
        print("Can't open the file. Close it in Excel and try again.\n")    


    


print("\nImported data:")
print(data)

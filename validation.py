from pathlib import Path

import pandas as pd


# ---------- Checks ----------

def check_path(file_path):
    file_path = Path(str(file_path).strip().strip('"'))
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")
    if file_path.suffix.lower() != ".xlsx":
        raise ValueError("Please provide an Excel (.xlsx) file.")
    return file_path


def check_sheet(file_path, sheet_number):
    sheets = pd.ExcelFile(file_path).sheet_names
    if sheet_number < 0 or sheet_number >= len(sheets):
        raise ValueError(f"Sheet does not exist. This file has {len(sheets)} sheet(s).")


def check_header(header_row):
    if header_row < 0:
        raise ValueError("Header row must be 1 or higher.")


# ---------- Prompts (ask the user until the answer passes the checks) ----------

def ask_number(prompt):
    """Ask for a whole number >= 1. Returns it in Python counting (from 0)."""
    while True:
        try:
            number = int(input(prompt)) - 1
        except ValueError:
            print("Please enter a whole number.\n")
            continue
        if number < 0:
            print("Please enter 1 or higher.\n")
        else:
            return number


def ask_file_path():
    while True:
        try:
            return check_path(input("Enter the Excel file path: "))
        except (FileNotFoundError, ValueError) as error:
            print(f"{error}\n")


def ask_sheet(file_path):
    sheets = pd.ExcelFile(file_path).sheet_names

    print("The available sheets are:")
    for i, name in enumerate(sheets, start=1):
        print(f"{i}. {name}")

    while True:
        sheet_number = ask_number("Enter sheet number: ")
        try:
            check_sheet(file_path, sheet_number)
        except ValueError as error:
            print(f"{error}\n")
            continue
        return sheet_number


def ask_header():
    return ask_number("Enter the header row #: ")

import pandas as pd

def check_formula(data, formula):
    result = data.eval(formula)
    if not isinstance(result, pd.Series):
        raise ValueError("Formula must use at least one column.")
    return result


def ask_formula(data, prompt):
    while True:
        formula = input(prompt)
        try:
            result = check_formula(data, formula)
        except NameError as error:
            print(f"Unknown column name: {error}.\n")
            continue
        except (SyntaxError, ValueError) as error:
            print(f"Invalid formula: {error}\n")
            continue
        return formula, result

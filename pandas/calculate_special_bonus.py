import pandas as pd


def main():
    data = {
        'employee_id': [2, 3, 7, 8, 9],
        'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
        'salary': [3000, 3800, 7400, 6100, 7700]
    }

    employees_df = pd.DataFrame(data)
    
    result_df = calculate_special_bonus(employees_df)
    print(result_df)


def bonus_rule(row: pd.Series) -> int:
    if row['employee_id'] % 2 == 1 and not row['name'].startswith('M'):
        return row['salary']
    else:
        return 0


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(bonus_rule, axis=1)
    return employees[['employee_id', 'bonus']].sort_values('employee_id')


if __name__ == '__main__':
    main()
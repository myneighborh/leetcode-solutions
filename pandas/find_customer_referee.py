import pandas as pd


def main():
    data = {
        'id': [1, 2, 3, 4, 5, 6],
        'name': ['Will', 'Jane', 'Alex', 'Bill', 'Zack', 'Mark'],
        'referee_id': [None, None, 2, None, 1, 2]
    }
    
    df = pd.DataFrame(data)

    result = find_customer_referee(df)
    print(result.to_string(index=False))


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    result = customer[(customer['referee_id'] != 2) | (customer['referee_id'].isna())]
    return result[['name']]


if __name__ == '__main__':
    main()
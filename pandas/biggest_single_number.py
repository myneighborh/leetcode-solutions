import pandas as pd


def main():
    df1 = pd.DataFrame({
        'num': [8, 8, 3, 3, 1, 4]
    })
    df2 = pd.DataFrame({
        'num': [8, 8, 7, 7, 3, 3]
    })

    result1 = biggest_single_number(df1)
    print("Example 1:")
    print(result1.to_string(index=False))

    result2 = biggest_single_number(df2)
    print("Example 2:")
    print(result2.to_string(index=False))


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers['num'].value_counts()
    single_numbers = counts[counts == 1].index
    result = max(single_numbers) if len(single_numbers) > 0 else None
    return pd.DataFrame({'num': [result]})


if __name__ == '__main__':
    main()
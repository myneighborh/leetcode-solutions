import pandas as pd


def main():
    data = {
        'product_id': [0, 1],
        'store1': [95, 70],
        'store2': [100, None],
        'store3': [105, 80]
    }
    df = pd.DataFrame(data) 
    output = rearrange_products_table(df)
    print(output)

    
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    melted = products.melt(
        id_vars=['product_id'],
        value_vars=['store1', 'store2', 'store3'],
        var_name='store',
        value_name='price'
    )

    result = melted.dropna(subset=['price'])

    return result


if __name__ == '__main__':
    main()
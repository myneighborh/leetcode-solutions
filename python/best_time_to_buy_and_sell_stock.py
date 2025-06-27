from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit
    

def main():
    sol = Solution()
    example_list = [[7,1,5,3,6,4], [7,6,4,3,1]]
    
    for i, example in enumerate(example_list):
        result = sol.maxProfit(example)
        print(f"Example {i + 1}: {result}")


if __name__ == '__main__':
    main()
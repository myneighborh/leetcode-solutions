from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(p) for p in permutations(nums)]
    

def main():
    input_list = [
        [1, 2, 3],
        [0, 1],
        [1]
    ]

    sol = Solution()

    for input in input_list:
        result = sol.permute(input)
        print(result)


if __name__ == '__main__':
    main()
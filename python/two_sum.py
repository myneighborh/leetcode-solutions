from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []
    

def main():
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = sol.twoSum(nums, target)
    print(f"Input: {nums}, Target: {target}, Result: {result}")


if __name__ == '__main__':
    main()
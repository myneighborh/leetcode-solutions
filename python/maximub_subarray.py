# Given an integer array nums, find the subarray with the largest sum, and return its sum.


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
    

def main():
    nums_list = [[-2,1,-3,4,-1,2,1,-5,4],
                [1],
                [5,4,-1,7,8]]
    
    sol = Solution()
    for nums in nums_list:
        result = sol.maxSubArray(nums)
        print(result)


if __name__ == '__main__':
    main()
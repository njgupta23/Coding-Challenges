# Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def maxSum(nums):
    max_sum = curr_sum = nums[0]
    
    for n in nums[1:]:
        curr_sum = max(n, n + curr_sum)
        max_sum = max(curr_sum, max_sum)
    
    return max_sum

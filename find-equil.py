# Given a list of unordered integers,
# find the equilibrium point where the sum of all ints to the left 
# equals the sum of all ints to the right.

# Notes:
#     - Return the index of the last element in the first half of the list
#     - If there is no exact equilibrium point, return the closest

# >>> nums = [5, 3, 2, 4, 6]
# >>> find_equilibrium(nums)
# 2

# >>> nums = [2, 4, 3, 1, 2, 1, 5]
# >>> find_equilibrium(nums)
# 2

# >>> nums = [2, 1, 3]
# >>> find_equilibrium(nums)
# 1

def find_eq(nums):

    left = 0
    right = len(nums) - 1
    Lsum = nums[left]
    Rsum = nums[right]

    while left < right - 1:
        if Lsum < Rsum:
            left += 1
            Lsum += nums[left]
        else:
            right -= 1
            Rsum += nums[right]

    return left

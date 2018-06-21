# Pairs of 100

# Given a list of positive integers, 
# return a list of pairs that add up to 100.

# Integers should be used only once 
# (unless they appear multiple times in the list)

# examples:

# [2, 99, 98]
# > [[2, 98]]

# [1, 97, 99, 3]
# > [[1, 99], [97, 3]]

# [1, 99, 99, 1]
# > [[1, 99], [99, 1]]


def get_pairs(nums):

    output = []

    for num in nums:
        pair = []
        save = num
        for i in range(len(nums)):
            if nums[i] == 100 - save:
                pair.append(save)
                pair.append(nums[i])
                output.append(pair)
                break

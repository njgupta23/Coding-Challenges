# Given a non-empty array, return true if there is a place to split the array 
# so that the sum of the numbers on one side is equal to the sum of the numbers 
# on the other side.


# canBalance([1, 1, 1, 2, 1]) → true
# canBalance([2, 1, 1, 2, 1]) → false
# canBalance([10, 10]) → true


def canBalance(nums):

	count = len(nums) - 2
	i = 0
	j = -1
	sumL = nums[i]
	sumR = nums[j]

	while count > 0:

		if sumL == sumR:
			count -= 2
			i += 1
			j -= 1
			sumL += nums[i]
			sumR += nums[j]

		elif sumL < sumR:
			count -= 1
			i += 1
			sumL += nums[i]

		else:
			count -= 1
			j -= 1
			sumR += nums[j]

	if sumL == sumR:
		return True
	else:
		return False



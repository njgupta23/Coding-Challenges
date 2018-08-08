# Write a function that returns true if the givin list
# of integers containsa pair that adds to the given sum, 
# or false if it does not.

# ex 1:
# nums = [1, 2, 3, 9]
# sum = 8
# return false

# ex 2: 
# nums = [1, 2, 4, 4]
# sum = 8
# return true


def has_sum(nums, s):

	comp = set()

	for n in nums:
		 if n in comp:
		 	return True
		 else:
		 	comp.add(s-n)

	return False

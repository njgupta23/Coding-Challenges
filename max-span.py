# Max Span


# Consider the leftmost and righmost appearances of some value in an array. 
# We'll say that the "span" is the number of elements between the two inclusive. 
# A single value has a span of 1. Returns the largest span found in the given array. 
# (Efficiency is not a priority.)


# maxSpan([1, 2, 1, 1, 3]) → 4
# maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
# maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6


def max-span(nums):
	max_span = 1

	for i in range(len(nums)):
		n = nums[i]
		span = 1

		for j in range(len(nums)-1, i, -1):
			if nums[j] == n:
				span = j - i + 1
			if span > max_span:
				max_span = span

	return max_span
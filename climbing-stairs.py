# Climbing Stairs

# Imagine, on a flight of stairs, that you can climb either 1, 2, or 3 steps at a time.

# One a staircase with three steps, you could do this in 4 different ways:

# take 1 step, 1 step, and 1 step (“111”)
# take 1 step, and 2 steps (“12”)
# take 2 steps and 1 step (“21”)
# take 3 steps (“3”)
# On a staircase with 4 steps, you could this 7 ways: “1111”, “121”, “211”, “112”, “22”, “13”, “31”.

# Write a function that calculates the number of ways you could climb a staircase of n steps.


def steps(n):

	if n == 0:
		return 1
	if n < 0:
		return 0

	if n > 0:
		return steps(n-1) + steps(n-2) + steps(n-3)


# More efficient method, which stores previously computed permutations:

def steps_cache(n):

	cache = [None] * (n+1)

	def _steps(n):

		if n == 0:
			return 1
		if n < 0:
			return 0

		if cache[n] is None:
			cache[n] = _steps(n-1) + _steps(n-2) + _steps(n-3)

		return cache[n]

	return _steps(n)


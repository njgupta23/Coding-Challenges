# Without String


# Given two strings, base and remove, return a version of the base string where all 
# instances of the remove string have been removed. 
# You may assume that the remove string is length 1 or more. 
# Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".


# withoutString("Hello there", "llo") → "He there"
# withoutString("Hello there", "e") → "Hllo thr"
# withoutString("Hello there", "x") → "Hello there"


def withoutStr(base, remove):
	new = ""
	length = len(remove)
	count = 0

	for i in range(len(base)):

		if count > 0:
			count -= 1
			continue

		if base[i] != remove[0]:
			new += base[i]

		else:
			if base[i:(i+length)] == remove:
				count = length - 1
			else:
				new += base[i]

	return new


# Sum Numbers

# Given a string, return the sum of the numbers appearing in the string, 
# ignoring all other characters. A number is a series of 1 or more digit chars in a row. 
# (Note: isdigit() tests if a char is one of the chars '0', '1', .. '9'. 
# 	int() converts a string to an int.)


# sumNumbers("abc123xyz") → 123
# sumNumbers("aa11b33") → 44
# sumNumbers("7 11") → 18


def sumNums(s):
	sum = 0
	count = 0
	
	for i in range(len(s)):
		num_str = '0'

		if count > 0:
			count -= 1
			continue

		if s[i].isdigit():

			for j in range(i, len(s)):
				if s[j].isdigit():
					num_str += s[j]
					count += 1
				else:
					break

		sum += int(num_str)

	return sum

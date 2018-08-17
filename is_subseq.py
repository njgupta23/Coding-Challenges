# Is Subsequence

# Write a function that returns True if string b is a subsequence
# of string a and False if not. 

# ex:
# isSubseq('abppleee', 'ale') => True
# isSubseq('abppleee', 'bale') => False


def isSubseq(a, b):

	a_idx = 0
	b_idx = 0

	while a_idx < len(a) and b_idx < len(b):
		if a[a_idx] == b[b_idx]:
			b_idx += 1
		a_idx += 1

	return b_idx == len(b)



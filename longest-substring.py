# s = 'abppplee'
# d = ['able', 'ale', 'apple', 'bale', 'kangaroo']
# return 'apple'


# def longest_substring(s,d):
# 	longest = ''

# 	for w in d:
# 		i = 0
# 		for char in s:
# 			if char == w[i]:
# 				i++
# 			if i == len(w) and len(w) > len(longest):
# 				longest = w

# 	return longest


def longest_substr(s, d):

	longest = ''

	for w in d:

		w_idx = 0
		s_idx = 0

		while s_idx<len(s) and w_idx<len(w):
			if s[s_idx] == w[w_idx]:
				w_idx += 1
			s_idx += 1

		if w_idx == len(w) and len(w) > len(longest):
			longest = w

	return longest